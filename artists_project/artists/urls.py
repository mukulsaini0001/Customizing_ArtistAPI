from django.urls import path
from .views import (
    WorkListView,
    WorkDetailView,
    ArtistListView,
    ArtistDetailView,
    CustomObtainAuthToken,
    UserRegistrationView,
)

urlpatterns = [
    path('api/works/', WorkListView.as_view(), name='work-list'),
    path('api/works/<int:pk>/', WorkDetailView.as_view(), name='work-detail'),
    path('api/artists/', ArtistListView.as_view(), name='artist-list'),
    path('api/artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('api/login/', CustomObtainAuthToken.as_view(), name='user-login'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
]







