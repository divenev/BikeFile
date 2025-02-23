from enum import Enum

from django.core.validators import URLValidator
from django.db import models

from BikeFile.address.models import Address
from BikeFile.appuser.models import AppUser
from other_functionalities.validators import MinRequirementChars
from other_functionalities.choices_enum import ChoicesEnum

MAX_TYPE_BIKE_LENGTH = 30
MAX_BRAND_LENGTH = 30
MAX_MODEL_LENGTH = 30
MAX_CODE_LENGTH = 10
MAX_FRAME_NUMBER_LENGTH = 30
MIN_FRAME_NUMBER_LENGTH = 5
MAX_FRAME_SIZE_LENGTH = 5
MAX_URL_LENGTH = 2050
VALIDATOR_MESSAGE = 'The frame_number is too short.'
# typeBike
# ADVENTURE = 'Adventure / Touring'
# BMX = 'BMX'
# CITY = 'City'
# CLASSIC = 'Classic'
# ELECTRIC = 'Electric'
# FAT_TIRE = 'Fat tire'
# FOLDING = 'Folding'
# HYBRID = 'Hybrid'
# KID = 'Kid'
# MTB = 'Mountain'
# RECUMBENT = 'Recumbent'
# ROAD = 'Road'
# TANDEM = 'Tandem'
# WOMEN = 'Women’s'
# ANOTHER = 'Another'
# status
NOT_FOR_SALE = 'not for sale'
FOR_SALE = 'for sale'
STOLEN = 'stolen'


# class TypeBikeChoices(ChoicesEnum, Enum):
#     adventure = ADVENTURE
#     bmx = BMX
#     city = CITY
#     classic = CLASSIC
#     electric = ELECTRIC
#     fat_tire = FAT_TIRE
#     folding = FOLDING
#     hybrid = HYBRID
#     kid = KID
#     mtb = MTB
#     recumbent = RECUMBENT
#     road = ROAD
#     tandem = TANDEM
#     women = WOMEN
#     another = ANOTHER


class StatusBikeChoices(ChoicesEnum, Enum):
    not_for_sale = NOT_FOR_SALE
    for_sale = FOR_SALE
    stolen = STOLEN


class TypeBike(models.Model):
    name = models.CharField(
        max_length=MAX_TYPE_BIKE_LENGTH,
        null=False,
        blank=False,
    )

    code = models.CharField(
        max_length=MAX_CODE_LENGTH,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'


class GalleryBike(models.Model):
    img_url = models.URLField(
        max_length=MAX_URL_LENGTH,
        validators=[URLValidator(), ],
        null=True,
        blank=True,
    )

    img = models.ImageField(
        upload_to='media/gallery_bike',
        null=True,
        blank=True,
    )

    default = models.BooleanField(
        default=False,
    )


class DocumentImg(models.Model):
    img_url = models.URLField(
        max_length=MAX_URL_LENGTH,
        validators=[URLValidator(), ],
        null=True,
        blank=True,
    )

    img = models.ImageField(
        upload_to='media/document_img',
        null=True,
        blank=True,
    )


class Bike(models.Model):
    frame_number = models.CharField(
        max_length=MAX_FRAME_NUMBER_LENGTH,
        validators=[
            MinRequirementChars(min_string_length=MIN_FRAME_NUMBER_LENGTH, validator_message=VALIDATOR_MESSAGE)],
        null=False,
        blank=False,
    )

    # type_bike = models.CharField(
    #     max_length=MAX_TYPE_BIKE_LENGTH,
    #     default=ADVENTURE,
    #     choices=TypeBikeChoices.choices(),
    # )
    type_bike = models.ForeignKey(
        TypeBike,
        on_delete=models.RESTRICT,
        verbose_name='type bike',
        null=False,
        blank=False,
    )

    brand = models.CharField(
        max_length=MAX_BRAND_LENGTH,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        null=False,
        blank=False,
    )

    tire_size = models.FloatField(
        verbose_name='tire size',
    )

    frame_size = models.CharField(
        max_length=MAX_FRAME_SIZE_LENGTH,
        verbose_name='frame size'
    )

    status = models.CharField(
        default=NOT_FOR_SALE,
        choices=StatusBikeChoices.choices(),
    )

    img = models.ForeignKey(
        GalleryBike,
        on_delete=models.RESTRICT,
        verbose_name='image bike',
        null=True,
        blank=True
    )

    doc_img = models.ForeignKey(
        DocumentImg,
        on_delete=models.RESTRICT,
        verbose_name='document img',
        null=True,
        blank=True
    )

    price_for_sale = models.FloatField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    location = models.ForeignKey(
        Address,
        on_delete=models.RESTRICT,
        verbose_name='address',
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        verbose_name='owner',
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    update_date = models.DateTimeField(
        auto_now=True,
    )

    is_delete = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.brand} - {self.model} - {self.type_bike}'
