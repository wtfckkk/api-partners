from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet, base_name='partners')

partners_router = NestedDefaultRouter(router, r'partners', lookup='partners')

urlpatterns = router.urls
urlpatterns += partners_router.urls
