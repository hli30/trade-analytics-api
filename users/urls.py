from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import AccountViewSet

router = DefaultRouter()
router.register(r'', AccountViewSet)

urlpatterns = [
    path('login/', views.obtain_auth_token, name='login')
]

urlpatterns += router.urls

