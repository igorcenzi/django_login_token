from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from .serializers import UserSerializer

# Create your views here.
class UserView(APIView):
  def post(self, request):
    user = UserSerializer(data=request.data)
    user.is_valid(raise_exception=True)
    user.save()
    return Response(user.data, status.HTTP_201_CREATED)