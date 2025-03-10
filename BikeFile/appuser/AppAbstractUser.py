from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.core.validators import RegexValidator

from BikeFile.appuser.AppUserManager import AppUserManager

MAX_STRING_LENGTH = 50
MAX_PHONE_LENGTH = 20
PHONE_REGEX = '^[+0-9]+'
EMAIL_REGEX = '^[a-z0-9]+[\._]?[ a-z0-9_]+[@]\w+[. ]\w{2,3}$'


class AppAppUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        unique=True,
        max_length=MAX_STRING_LENGTH,
        validators=[RegexValidator(regex=EMAIL_REGEX,
                                   message='Enter a valid email',
                                   code='invalid_email')],
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_STRING_LENGTH,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_STRING_LENGTH,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        max_length=MAX_PHONE_LENGTH,
        validators=[RegexValidator(regex=PHONE_REGEX,
                                   message='Enter a valid phone number',
                                   code='invalid_phone_number')],
        null=True,
        blank=True,
    )

    update_date = models.DateTimeField(
        auto_now=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)