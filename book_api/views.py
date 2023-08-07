from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 

from book_api.models import Book
from book_api.serializer import BookSerializer
# Create your views here.

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()  # complex
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['POST','PUT','DELETE'])   
def book(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method=="PUT":
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return (serializer.errors, status==status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        book.delete()
        return Response(
            status =status.HTTP_204_NO_CONTENT
        )