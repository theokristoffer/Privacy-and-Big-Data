# Generated by Django 4.2.16 on 2024-11-16 16:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wger.gym.models.user_document


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('owner', models.CharField(blank=True, max_length=100, null=True, verbose_name='Owner')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='ZIP code')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=30, null=True, verbose_name='Street')),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('gym_trainer', 'Trainer: can see the users for a gym'), ('manage_gym', 'Admin: can manage users for a gym'), ('manage_gyms', 'Admin: can administrate the different gyms')),
            },
        ),
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
                ('document', models.FileField(upload_to=wger.gym.models.user_document.gym_document_upload_dir, verbose_name='Document')),
                ('original_name', models.CharField(editable=False, max_length=128)),
                ('name', models.CharField(blank=True, help_text='Will use file name if nothing provided', max_length=60, verbose_name='Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('member', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='userdocument_member', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='userdocument_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp_created'],
            },
        ),
        migrations.CreateModel(
            name='GymConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeks_inactive', models.PositiveIntegerField(default=4, help_text='Number of weeks since the last time a user logged his presence to be considered inactive', verbose_name='Reminder of inactive members')),
                ('show_name', models.BooleanField(default=False, help_text='Show the name of the gym in the site header', verbose_name='Show name in header')),
                ('gym', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='config', to='gym.gym')),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gym', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ContractOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gym', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Amount')),
                ('payment', models.CharField(choices=[('1', 'Yearly'), ('2', 'Half yearly'), ('3', 'Monthly'), ('4', 'Biweekly'), ('5', 'Weekly'), ('6', 'Daily')], default='3', help_text='How often the amount will be charged to the member', max_length=2, verbose_name='Payment type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Contract is active')),
                ('date_start', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start date')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='ZIP code')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=30, null=True, verbose_name='Street')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('profession', models.CharField(blank=True, max_length=50, null=True, verbose_name='Profession')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('contract_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.contracttype', verbose_name='Contract type')),
                ('member', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='contract_member', to=settings.AUTH_USER_MODEL)),
                ('options', models.ManyToManyField(blank=True, to='gym.contractoption', verbose_name='Options')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='contract_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_start'],
            },
        ),
        migrations.CreateModel(
            name='AdminUserNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(verbose_name='Note')),
                ('member', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='adminusernote_member', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='adminusernote_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp_created'],
            },
        ),
        migrations.CreateModel(
            name='GymUserConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('include_inactive', models.BooleanField(default=True, help_text='Include this user in the email list with inactive members', verbose_name='Include in inactive overview')),
                ('gym', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('gym', 'user')},
            },
        ),
        migrations.CreateModel(
            name='GymAdminConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview_inactive', models.BooleanField(default=True, help_text='Receive email overviews of inactive members', verbose_name='Overview of inactive members')),
                ('gym', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('gym', 'user')},
            },
        ),
    ]
