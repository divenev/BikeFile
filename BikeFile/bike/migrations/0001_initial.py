# Generated by Django 4.2.3 on 2023-07-14 20:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import other_functionalities.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(blank=True, max_length=2050, null=True, validators=[django.core.validators.URLValidator()])),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/document_img')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(blank=True, max_length=2050, null=True, validators=[django.core.validators.URLValidator()])),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/gallery_bike')),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_number', models.CharField(max_length=30, validators=[other_functionalities.validators.MinRequirementChars(min_string_length=5, validator_message='The frame_number is too short.')])),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('tire_size', models.IntegerField(verbose_name='tire size')),
                ('frame_size', models.CharField(max_length=5, verbose_name='frame size')),
                ('status', models.CharField(choices=[('not_for_sale', 'not for sale'), ('for_sale', 'for sale'), ('stolen', 'stolen')], default='not for sale')),
                ('price_for_sale', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('doc_img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='bike.documentimg', verbose_name='document_img')),
                ('img', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='bike.gallerybike', verbose_name='image bike')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='address.address', verbose_name='Address')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('type_bike', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bike.typebike', verbose_name='type bike')),
            ],
        ),
    ]
