from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet)

urlpatterns = router.urls