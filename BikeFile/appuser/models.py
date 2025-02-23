from django.db import models
from enum import Enum

from BikeFile.address.models import Language, Address
from BikeFile.appuser.AppAbstractUser import AppAppUser
from other_functionalities.choices_enum import ChoicesEnum

MAX_STRING_LENGTH = 50
MIN_STRING_LENGTH = 5
VALIDATOR_MESSAGE = 'The username is too short.'
MAX_PHONE_LENGTH = 20
ADMINISTRATOR = 'administrator'
USER = 'user'
READ_ONLY = 'read_only'
PHONE_REGEX = '^[+0-9]+'
EMAIL_REGEX = '^[a-z0-9]+[\._]?[ a-z0-9_]+[@]\w+[. ]\w{2,3}$'


class GroupChoices(ChoicesEnum, Enum):
    administrator = ADMINISTRATOR
    user = USER
    read_only = READ_ONLY


class AppUser(AppAppUser):
    address = models.ForeignKey(
        Address,
        on_delete=models.RESTRICT,
        verbose_name='Address',
        null=True,
        blank=True,
    )

    role = models.CharField(
        max_length=MAX_STRING_LENGTH,
        default=USER,
        choices=GroupChoices.choices(),
        null=False,
        blank=False
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.RESTRICT,
        verbose_name='language',
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
