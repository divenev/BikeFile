from django.db import models

MAX_LENGTH_NAMES = 50
MAX_LENGTH_CODE = 10
MAX_LENGTH_ADDRESS = 60


class Country(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        unique=True,
        null=False,
        blank=False)

    code = models.CharField(
        max_length=MAX_LENGTH_CODE,
        null=False,
        blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        unique=True,
        null=False,
        blank=False)

    code = models.CharField(
        max_length=MAX_LENGTH_CODE,
        null=True,
        blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False)

    code = models.CharField(
        max_length=MAX_LENGTH_CODE,
        null=True,
        blank=True)

    country_id = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
        verbose_name='country'
    )

    def __str__(self):
        return f'{self.name} - {self.country_id}'


class City(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
        null=False,
        blank=False)

    postCode = models.CharField(
        max_length=MAX_LENGTH_CODE,
        null=True,
        blank=True)

    code = models.CharField(
        max_length=MAX_LENGTH_CODE,
        null=True,
        blank=True)

    country_id = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
        verbose_name='country'
    )

    region_id = models.ForeignKey(
        Region,
        on_delete=models.RESTRICT,
        verbose_name='region'
    )

    def __str__(self):
        return f'{self.name}, {self.region_id}'


class Address(models.Model):
    country_id = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
        verbose_name='country'
    )

    region_id = models.ForeignKey(
        Region,
        on_delete=models.RESTRICT,
        verbose_name='region'
    )

    city_id = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
        verbose_name='city'
    )

    address = models.CharField(
        max_length=MAX_LENGTH_ADDRESS,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.address}, {self.city_id}'
