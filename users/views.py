from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# class LoginView(APIView):
#     permission_classes = ()

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    