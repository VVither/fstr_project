from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .serializers import PerevalSerializer
from .models import pereval_added

class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "mesage": "Данные успешно сохранены"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "mesage": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            try:
                pereval = get_object_or_404(pereval_added, pk=pk)
                serializer = PerevalSerializer(pereval)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'state': 0, 'message': f'Перевал с ID {pk} не найден'}, status=status.HTTP_404_NOT_FOUND)
        else:
            email = request.query_params.get('user__email=email')    
            if email:
                perevals = pereval_added.objects.filter(user__email=email)
                serializer = PerevalSerializer(perevals, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'state': 0, 'message': 'Не передан Email'}, status=status.HTTP_400_BAD_REQUEST) 
                        
    def patch(self, request, pk):
        try:
            pereval = get_object_or_404(pereval_added, pk=pk)
            if pereval.status != 'new':
                return Response({"state": 0, "message": "Перевал можно редактировать только со статусом 'new'"}, status=status.HTTP_400_BAD_REQUEST)
            
            editable_fields = [
                'beautyTitle',
                'title',
                'other_titles',
                'connect',
                'coords_id',
                'winter_level',
                'summer_level',
                'autumn_level',
                'spring_level',
                'images'
            ]
            data = request.data.copy()

            for field in list(data.keys()):
                if field not in editable_fields:
                    del data[field]

            serializer = PerevalSerializer(pereval, data=data, pereval=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"state": 1, "message": "Данные успешно изменены"}, status=status.HTTP_200_OK)
            else:
                return Response({"state": 0, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"state": 0, "message": f"Перевал с ID {pk} не найден"}, status=status.HTTP_404_NOT_FOUND)