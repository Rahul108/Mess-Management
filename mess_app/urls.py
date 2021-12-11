from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from mess_app.views import MessViewSet, MessNUserViewSet

router = DefaultRouter()
router.register(r'mess',MessViewSet)
router.register(r'mess_n_user', MessNUserViewSet)

urlpatterns = []
urlpatterns += router.urls