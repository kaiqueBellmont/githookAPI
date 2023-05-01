from rest_framework.views import APIView
from rest_framework.response import Response
from api.analizer.code_analizer import AnalizeCode
import requests

class CodeAnalizer(APIView):
    """
    Teste
    """

    def get(self, request):
        """
        :param request:
        """
        req = requests.get("http://0.0.0.0:9000/")
        req = req.json()
        print(req)
        return Response(req)

    def post(self, request):
        """
        :param request:
        :return:
        """
        data = AnalizeCode.analyze(request.data)
        return Response(data)
