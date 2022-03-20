from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from expense_app.views import CostCategoryViewSet, MessEventNCostCategoryNUserCostViewSet, TotalCostOfMess

router = DefaultRouter()
router.register(r'cost_category', CostCategoryViewSet)
router.register(r'mess_event_n_cost_category_n_user_cost', MessEventNCostCategoryNUserCostViewSet)
router.register(r'mess-cost-overview', TotalCostOfMess)

urlpatterns = []
urlpatterns += router.urls