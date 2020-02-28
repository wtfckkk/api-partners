from rest_framework import routers
from partners.urls import router as partners_router
from partners.urls import urlpatterns as partners_urlpatterns

router = routers.DefaultRouter()
router.registry.extend(partners_router.registry)

urlpatterns = []
urlpatterns += partners_urlpatterns
urlpatterns += router.urls
