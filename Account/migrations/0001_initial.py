# Generated by Django 3.2.5 on 2021-08-26 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('body', models.TextField(blank=True, max_length=500, null=True, verbose_name='About')),
                ('Date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='experience_pictures/', verbose_name='user_experience')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('amount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Amount')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_pictures/', verbose_name='user_pictures')),
                ('about_me', models.TextField()),
                ('job', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='Github')),
                ('skype', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skype')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='Twitter')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
