from rest_framework import generics
from BikeFile.bike.models import Bike, GalleryBike
from BikeFile.bike.serializers import BikeSerializer


class UserBikesListAPIView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    def post(self, request, *args, **kwargs):
        request.data['owner'] = self.request.user.id
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user)


class CheckBikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    def get_queryset(self):
        frame_number = self.request.query_params.get('frame_number')
        if frame_number:
            return self.queryset.filter(frame_number=frame_number)


class BikeDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIViauth_group_permissionsew
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        request.data['owner'] = self.request.user.id
        return self.update(request, *args, **kwargs)

    def get_queryset(self):
        bike_id = self.kwargs.get('pk')
        return self.queryset.filter(id=bike_id, owner_id=self.request.user)

    def perform_destroy(self, instance):
        img_id = instance.img.id
        instance.delete()
        if img_id:
            GalleryBike.objects.filter(id=img_id).delete()

