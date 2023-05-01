from rest_framework.views import APIView
from rest_framework.response import Response
from api.analizer.code_analizer import AnalizeCode
from .requester import requester


class CodeAnalizer(APIView):
    """
    Teste
    """

    def get(self, request):
        """
        :param request:
        """
        req = requester.GitHookApiRequester()
        res = req.request.get(req.params.OPEN_AI_WORKER_ENDPOINT)

        return Response(res.json())

    def post(self, request):
        """
        :param request:
        :return:
        """
        req = requester.GitHookApiRequester()

        open_ai_insight_response = req.request.post(
            url=req.params.OPEN_AI_WORKER_ENDPOINT+"insight",
            json=request.data
        )

        data = AnalizeCode.analyze(request.data)

        if open_ai_insight_response.status_code == 200:
            result = open_ai_insight_response.json()
            # Processar o resultado retornado
            print(result)
            print(data)

            result = {"code": data, "insight": open_ai_insight_response}
            return Response(result)
        else:
            print("Erro na solicitação:", open_ai_insight_response.status_code, open_ai_insight_response.text)
            return Response("Erro na solicitação:", open_ai_insight_response.status_code, open_ai_insight_response.text)
