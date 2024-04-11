from django.urls import path,include,re_path
from .views import FlowerList
from rest_framework.routers import DefaultRouter

post_router=DefaultRouter()
post_router.register('flower',FlowerList,basename='flower')


# urlpatterns = post_router.urls