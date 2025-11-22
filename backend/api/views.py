from rest_framework.response import Response
from rest_framework.views import APIView

from .versions import Versioning


class HelloWorldView(APIView):
    versioning_class = Versioning

    def get(self, request, *args, **kwargs):
        version = request.version

        if version == "v1":
            return Response(data={"message": "Hello, World! v1"})
        elif version == "v2":
            return Response(data={"message": "Hello, World! v2"})
