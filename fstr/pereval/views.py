from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerevalSerializer

class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "mesage": "Данные успешно сохранены"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "mesage": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
