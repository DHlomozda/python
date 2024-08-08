# Generated by Django 5.1 on 2024-08-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellable',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('is_Reserved', models.BooleanField(default=False)),
                ('photo_Url', models.TextField()),
                ('is_bought', models.BooleanField(default=False)),
            ],
        ),
    ]
