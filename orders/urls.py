from rest_framework import routers
from orders.views import OrderViewSet, CustomerViewSet

router = routers.SimpleRouter()

router.register(r'api/orders', OrderViewSet)
router.register(r'api/customers', CustomerViewSet)

urlpatterns = router.urls
