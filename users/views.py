from rest_framework import viewsets

from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Account.objects.all()
    serializer_class = AccountSerializer