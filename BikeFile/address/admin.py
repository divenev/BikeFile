from django.contrib import admin

from BikeFile.address.models import Country, Language, Region, City, Address

admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Address)

# Register your models here.
