# Generated by Django 3.2.6 on 2021-08-31 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_password', models.CharField(max_length=255)),
                ('user_validate', models.BooleanField(default=False)),
            ],
        ),
    ]
