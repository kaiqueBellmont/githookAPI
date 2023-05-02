import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.analizer.code_analizer import AnalizeCode
from .requester import requester


class CodeAnalizer(APIView):
    """
    Main class of the API.

    """

    def get(self, request) -> Response:
        """
        Makes the request to check if the worker is ok.
        :param request:
        """
        try:
            req = requester.GitHookApiRequester()
            res = req.request.get(req.params.OPEN_AI_WORKER_ENDPOINT)
            return Response(res.json())

        except requests.exceptions.RequestException:
            result = {"status": "OPEN_API_WORKER_ERROR: 500"}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request) -> Response:
        """
        :param request:
        :return:
        """

        # Analyze the modified files,
        # prepare the date
        # and check if it needs to call OpenAI

        data = AnalizeCode.analyze(request.data)
        result_code_values = data.values()
        all_empty = all(item == {} for item in result_code_values)

        # If there are no codes to be improved, it does not call the worker and returns the response faster.
        if all_empty:
            result = {"code": data, "insight": {}}
            return Response(result)

        # It makes requests to the OpenAI worker, even if it is OFF, it still works and saves resources.
        if not all_empty:
            try:
                req = requester.GitHookApiRequester()
                open_ai_insight_response = req.request.post(
                    url=req.params.OPEN_AI_WORKER_ENDPOINT + "insight",
                    json=request.data,
                )

            except requests.exceptions.RequestException:
                result = {"code": data, "insight": "OPEN_API_WORKER_ERROR: 500"}
                return Response(result, status=status.HTTP_200_OK)

            if open_ai_insight_response.status_code == status.HTTP_200_OK:
                result = {"code": data, "insight": open_ai_insight_response}
                return Response(result)

            else:
                print(
                    "Erro na solicitação:",
                    open_ai_insight_response.status_code,
                    open_ai_insight_response.text,
                )
                return Response(
                    "Erro na solicitação:",
                    open_ai_insight_response.status_code,
                    open_ai_insight_response.text,
                )
