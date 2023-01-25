from django.contrib import admin
from django.urls import path, include
from news.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),


]
