from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from mess_app.views import MessViewSet

router = DefaultRouter()
router.register(r'mess',MessViewSet)

urlpatterns = []
urlpatterns += router.urls