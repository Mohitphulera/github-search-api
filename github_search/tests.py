from django.test import TestCase
from unittest.mock import patch, Mock
from rest_framework.test import APIClient


class GithubSearchTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_search_github_users(self):
        response = self.client.post('/github/api/search/', {'search_type': 'users', 'search_text': 'arpan'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["total_count"] , 0)

    def test_search_github_repositories(self):
        response = self.client.post('/github/api/search/', {'search_type': 'repositories', 'search_text': 'hello-world'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data["total_count"], 0)

    def test_search_non_existing_github_users_and_repositories(self):
        response = self.client.post('/github/api/search/', {'search_type': 'users', 'search_text': 'xeonzolto'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_count"], 0)

        response = self.client.post('/github/api/search/', {'search_type': 'repositories', 'search_text': 'xeonzolto'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_count"], 0)


    def test_search_wrong_search_type(self):
        response = self.client.post('/github/api/search/', {'search_type': 'chess', 'search_text': 'xeonzolto'}, format='json')
        self.assertEqual(response.status_code, 404)


    def test_clear_cache(self):
        response = self.client.post('/github/api/clear-cache/')
        self.assertEqual(response.status_code, 200)

    