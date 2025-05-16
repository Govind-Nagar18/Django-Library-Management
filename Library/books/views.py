from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Books
from .serializers import Bookserializer

class BooksView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        books = Books.objects.all()
        serializer = Bookserializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Message': 'Book has been added successfully!!'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BooksDetailsView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = Bookserializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({
                'Message': 'Data has been successfully updated'
            }, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, pk):
        book = Books.objects.get(pk=pk)
        book.delete()  
        return Response({
            'Message': 'Book has been deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)  


    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = Bookserializer(book)  
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT) 