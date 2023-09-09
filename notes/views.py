from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import NotesSerializer
from .models import Notes


class ListPagination(PageNumberPagination):
    page_size = 10


# Create your views here.
@api_view(["GET", "POST"])
def Notes_list(request):
    if request.method == "GET":
        paginator = ListPagination()
        notes = Notes.objects.all()
        result_page = paginator.paginate_queryset(notes, request)
        serializer = NotesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == "POST":
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
