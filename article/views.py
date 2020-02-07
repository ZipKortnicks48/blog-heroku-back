from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets, filters
from .models import Content,Subcategory
from .serializers import ContentSerializer
from rest_framework.generics import ListCreateAPIView,get_object_or_404,RetrieveUpdateDestroyAPIView
#получает ленту c фильтрами и прочим
class ContentLenthView(ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def perform_create(self,serializer):
        subcategory = get_object_or_404(Subcategory, id=self.request.data.get('subactegory'))
        return serializer.save(subactegory=subcategory)
class SingleContentView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    
    