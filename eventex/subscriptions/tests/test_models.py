#coding: utf-8
__author__ = 'lucianrocha'
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Lucian Marques Rocha',
            cpf= '03491946107',
            email='lucian.rochati@gmail.com',
            phone='67-91216537'
        )
    def test_create(self):
        'Subscrition must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'SUbscription mus have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at,datetime)

    def test_unicod(self):
        self.assertEqual(u'Lucian Marques Rocha',unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force the callision
        Subscription.objects.create(name='Lucian Marques', cpf='03191916107',
                                    email='lucian.rochati@gmail.com', phone='21-91216537')

    def test_cpf_unique(self):
        s = Subscription(name='Lucian Marques', cpf='03191916107',
                         email='outro@gmail.com', phone='21-91216537')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        s = Subscription(name='Lucian Marques', cpf='00000000011',
                         email='lucian.rochati@gmail.com', phone='21-91216537')
        self.assertRaises(IntegrityError, s.save)
