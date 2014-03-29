from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import API, Klass, Instance

class SmokeTest(TestCase):
    def test_admin(self):
        resp = self.client.get('/admin/')
        self.assertEqual(resp.status_code, 200)
    
    def test_homepage(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 404)
