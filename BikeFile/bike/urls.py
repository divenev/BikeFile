from django.urls import path
from BikeFile.bike.views import UserBikesListAPIView, CheckBikeListAPIView, BikeDetailsAPIView

urlpatterns = [
    path('bikes/', UserBikesListAPIView.as_view(), name='bikes_list'),
    path('details/<int:pk>', BikeDetailsAPIView.as_view(), name='bike_details'),
    path('check/', CheckBikeListAPIView.as_view(), name='bike_check'),

]
