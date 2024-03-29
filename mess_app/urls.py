from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from mess_app.views import MessEventViewSet, MessViewSet, MessNUserViewSet

router = DefaultRouter()
router.register(r'mess_info',MessViewSet)
router.register(r'mess_n_user', MessNUserViewSet)
router.register(r'mess_event', MessEventViewSet)

urlpatterns = []
urlpatterns += router.urls