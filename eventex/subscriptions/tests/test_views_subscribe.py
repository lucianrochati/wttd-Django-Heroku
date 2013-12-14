# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
# Create your tests here.

class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp,'<form')
        self.assertContains(self.resp,'<input', 6)
        self.assertContains(self.resp,'type="text"',3)
        self.assertContains(self.resp,'type="email"')
        self.assertContains(self.resp,'type="submit"')

    def test_csrf(self):
        'HTML musc contain csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form.'
        form = self.resp.context['form']
        self.assertIsInstance(form,SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Lucian Marques Rocha', cpf='12345678901',
                    email='lucian.rochati@gmail.com', phone='6791216537')
        self.resp = self.client.post('/inscricao/',data)

    def test_post(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST must be saved'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Lucian Marques Rocha', cpf='000000000012',
                    email='lucian.rochati@gmail.com',phone='67-91216537')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        'Invalid POST should not redirect.'
        self.assertEqual(200, self.resp.status_code)

    def test_form_erros(self):
        'form must contain erros'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())



