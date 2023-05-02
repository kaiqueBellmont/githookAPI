import unittest
from unittest.mock import patch

import requests
from rest_framework import status
from rest_framework.response import Response

from api.views import CodeAnalizer


class CodeAnalizerTestCase(unittest.TestCase):
    def setUp(self):
        self.analyzer = CodeAnalizer()

    def test_get_request_successful(self):
        with patch("api.requester.requester.GitHookApiRequester") as mock_requester:
            mock_request = mock_requester.return_value
            mock_response = Response()
            mock_response.json = lambda: {"status": "success"}
            mock_request.request.get.return_value = mock_response

            response = self.analyzer.get(None)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {"status": "success"})

    def test_get_request_failed(self):
        with patch("api.requester.requester.GitHookApiRequester") as mock_requester:
            mock_request = mock_requester.return_value
            mock_request.request.get.side_effect = requests.exceptions.RequestException(
                "Request failed"
            )

            response = self.analyzer.get(None)

            self.assertEqual(
                response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            self.assertEqual(response.data, {"status": "OPEN_API_WORKER_ERROR: 500"})

    def test_post_request_successful(self):
        request = type(
            "Request",
            (object,),
            {
                "data": {
                    "code_list": [
                        {
                            "hook/formatter.py": 'from dataclasses import dataclass\n\n\n@dataclass\nclass Formatter:\n    """\n    Formatter class\n    """\n\n    @staticmethod\n    def show_request_result(result):\n        """\n        :param result: Result from request\n        """\n        for file, erros in result.items():\n            print(f"Result for File: {file}:")\n            for line, messages in erros.items():\n                formatted_messages = "\\n\\t".join(messages)\n                print(f"Line {line}:\\n\\t{formatted_messages}")\n\n    @staticmethod\n    def show_in_code_format(codes):\n        """\n        print in python code format\n        :param: code\n            data = {\n                \\\'code_list\\\': code_list\n            }\n            # Example codes\n            codes = {\n                \\\'code_list\\\': [\n                    {\\\'exampl.py\\\': \\\'import datetime\\n\\ndef soma(a, b):\\n    return a + b\\\'},\n                    ]\n            }\n        """\n        for code in codes["code_list"]:\n            for filename, content in code.items():\n                print(f"File: {filename}")\n                print(content)\n'
                        }
                    ]
                }
            },
        )()

        with patch("api.requester.requester.GitHookApiRequester") as mock_requester:
            mock_request = mock_requester.return_value
            mock_response = Response()
            mock_response.json = lambda: {"status": "success"}
            mock_request.request.post.return_value = mock_response

            response = self.analyzer.post(request)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn("code", response.data)


if __name__ == "__main__":
    unittest.main()
