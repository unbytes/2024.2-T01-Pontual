from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Class, Status
from .serializers import ClassSerializer, StatusSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# Create your views here.

class ClassApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]


    def get(self, request, pk=None, user_id=None):
        """
        Recupera classes. Pode ser de um usuário específico ou do usuário autenticado.
        """
        if user_id:  # Filtrar classes de um usuário específico
            if not request.user.is_staff:  # Apenas administradores podem listar classes de outros usuários
                return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

            classes = Class.objects.filter(user_id=user_id)
            if not classes.exists():
                return Response({"detail": "No classes found for this user."}, status=status.HTTP_404_NOT_FOUND)
        elif pk:  # Recupera uma classe específica do usuário autenticado
            classes = Class.objects.filter(pk=pk, user=request.user)
        else:  # Recupera todas as classes do usuário autenticado
            classes = Class.objects.filter(user=request.user)

        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        """
        Handle POST requests to create a new Class.
        """
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associa o user autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Handle PATCH requests to partially update a Class.
        """
        class_instance = get_object_or_404(Class, pk=pk, user=request.user)
        serializer = ClassSerializer(class_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Class.
        """
        class_instance = get_object_or_404(Class, pk=pk, user=request.user)
        class_instance.delete()
        return Response({"detail": "Class deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class StatusApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, pk=None, user_id=None, year=None, month=None):
        """
        Recupera status de um usuário específico. 
        Se o `year` e `month` forem fornecidos, filtra os status por data.
        """
        if user_id:  # Buscar status de um usuário específico
            if not request.user.is_staff and request.user.id != user_id:
                return Response(
                    {"detail": "Permission denied."},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Filtro por usuário e, se fornecido, por ano e mês
            statuses = Status.objects.filter(classy__user_id=user_id)

            if year:
                statuses = statuses.filter(register__year=year)

            if month:
                statuses = statuses.filter(register__month=month)

            if not statuses.exists():
                return Response(
                    {"detail": "No statuses found for this user."},
                    status=status.HTTP_404_NOT_FOUND
                )
        elif pk:  # Buscar um status específico
            statuses = Status.objects.filter(pk=pk)
        else:  # Buscar todos os status
            statuses = Status.objects.all()

        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new Status object.
        """
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Fully update a Status object by ID.
        """
        status_instance = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(status_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partially update a Status object by ID.
        """
        status_instance = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(status_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a Status object by ID.
        """
        status_instance = get_object_or_404(Status, pk=pk)
        status_instance.delete()
        return Response({"detail": "Status deleted successfully."}, status=status.HTTP_204_NO_CONTENT)