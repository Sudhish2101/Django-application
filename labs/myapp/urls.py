from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/myapp', UserViewSet, 'myapp')

urlpatterns = router.urls