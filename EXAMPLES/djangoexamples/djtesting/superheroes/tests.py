from django.test import TestCase, tag
from django.urls import reverse

from .models import Superhero


class SuperheroTests(TestCase):

    fixtures = ['superheroes.json']

    def test_clark_kent_is_supermans_secret_identity(self):
        s = Superhero.objects.get(name='Superman')
        self.assertEquals('Clark Kent', s.secret_identity)

    def test_response_returns_200(self):
        response = self.client.get(
            reverse('superheroes:herodetails', args=('Superman',))
        )
        self.assertEqual(response.status_code, 200)

    def test_result_contains_expected_data(self):
        response = self.client.get(
            reverse('superheroes:herodetails', args=('Superman',))
        )
        self.assertIn(b'Superman', response.content)

    @tag('silly')
    def test_two_plus_two_is_four(self):
        self.assertEqual(2 + 2, 4)
