# Generated by Django 4.0.2 on 2022-02-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0002_delete_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=8)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
    ]