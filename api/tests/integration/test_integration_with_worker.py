import unittest
import requests
from rest_framework import status
from rest_framework.test import APIClient
import requests_mock
from api.utils.mocks import code_list
from api.requester.params import Params


class CodeAnalizerIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_request_when_all_empty(self):
        with requests_mock.Mocker() as mocker:
            params = Params()
            mocker.get(
                params.TEST_WORKER_ENDPOINT,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

            response = requests.get(params.TEST_WORKER_ENDPOINT)

            self.assertEqual(
                response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            self.assertEqual(dict(response), {})

    """
    
        def test_get_request_successful(self):
        res = requests.get(params.TEST_WORKER_ENDPOINT)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json(), {"state": "working"})
    """

    # The Worker needs to be offline

    def test_post_request_successful(self):
        data = code_list

        params = Params()

        response = requests.post(url=params.TEST_API_INTEGRATION_ENDPOINT, json=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("code", response.json())
        self.assertIn("insight", response.json())

    # for the tests below to pass, the worker must be down.
    """
    def test_get_request_failed(self):
        res = requests.get(params.TEST_WORKER_ENDPOINT)
        self.assertEqual(res.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(res.json(), {"status": "OPEN_API_WORKER_ERROR: 500"})
    """

    """
    def test_post_request_successful_when_worker_is_down(self):
        data = code_list
        params = Params()

        response = requests.post(
            url=params.TEST_API_INTEGRATION_ENDPOINT,
            json=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('code', response.json())
        self.assertIn('insight', response.json())
    """

    """
    def test_post_request_fail(self):
        data = {}

        params = Params()

        response = requests.post(
            url=params.TEST_API_INTEGRATION_ENDPOINT,
            json=data
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    """
