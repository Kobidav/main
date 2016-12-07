from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import CompInv


class QuestionMethodTests(TestCase):

    def question(self):
        response = self.client.get(reverse('inv'))
        self.assertEqual(response.status_code, 200)
