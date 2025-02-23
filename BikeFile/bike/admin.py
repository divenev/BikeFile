from django.contrib import admin

from BikeFile.bike.models import TypeBike, Bike, GalleryBike, DocumentImg

admin.site.register(TypeBike)
admin.site.register(Bike)
admin.site.register(GalleryBike)
admin.site.register(DocumentImg)