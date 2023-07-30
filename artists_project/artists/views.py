from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, permissions
from rest_framework.settings import api_settings
from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class WorkListView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class ArtistListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = UserSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


