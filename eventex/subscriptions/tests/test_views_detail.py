# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Lucian Marques Rocha', cpf='12345678901',
                                        email='lucian.rochati@gmail.com', phone='91216537')
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'Get /inscricao/1 should be status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Use template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'COntext must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'Lucian Marques Rocha')

class DetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404,response.status_code)
