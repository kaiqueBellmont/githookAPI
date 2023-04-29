from rest_framework.views import APIView
from rest_framework.response import Response
from api.analizer.code_analizer import AnalizeCode


class CodeAnalizer(APIView):
    """
    Teste
    """

    def get(self, request):
        """
        :param request:
        """
        print("Hello World")
        return Response({'message': 'Hello World'})

    def post(self, request):
        """
        :param request:
        :return:
        """
        data = AnalizeCode.analyze(request.data)
        return Response(data)
