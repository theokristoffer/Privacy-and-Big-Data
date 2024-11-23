# Generated by Django 4.2.16 on 2024-11-17 13:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wger.gallery.models.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Date')),
                ('image', models.ImageField(height_field='height', help_text='Only PNG and JPEG formats are supported', upload_to=wger.gallery.models.image.gallery_upload_dir, verbose_name='Image', width_field='width')),
                ('height', models.IntegerField(editable=False)),
                ('width', models.IntegerField(editable=False)),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
