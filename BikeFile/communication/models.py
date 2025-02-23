from django.db import models
from BikeFile.appuser.models import AppUser
from other_functionalities.validators import MinRequirementChars

MIN_STRING_LENGTH = 2
VALIDATOR_MESSAGE = 'The message is too short.'


class Messages(models.Model):
    sender = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        related_name='sender',
        verbose_name='sender',
    )

    receiver = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT,
        related_name='receiver',
        verbose_name='receiver',
    )

    text = models.TextField(
        validators=[MinRequirementChars(min_string_length=MIN_STRING_LENGTH, validator_message=VALIDATOR_MESSAGE), ],
        null=False,
        blank=False,
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )
