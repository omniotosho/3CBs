from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, ClassificationInsTypeViewSet, ClassificationProdTypeViewSet, ClosedAccountViewSet, ConsCommDetailsViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'classification_ins_types', ClassificationInsTypeViewSet)
router.register(r'classification_prod_types', ClassificationProdTypeViewSet)
router.register(r'closed_accounts', ClosedAccountViewSet)
router.register(r'cons_comm_details', ConsCommDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
