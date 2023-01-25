from rest_framework import viewsets, filters
from .models import News
from .serializers import NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-time_create')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]

    filterset_fields = ['title']
    ordering_fields = ['time_create']


