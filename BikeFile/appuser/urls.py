from django.urls import path
from BikeFile.appuser.views import RegisterAPIView, LoginAPIView
from knox import views as knox_views

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('register/', RegisterAPIView.as_view(), name='user_register'),
    path('logout/', knox_views.LogoutAllView.as_view(), name='user_logoutall'),
]
