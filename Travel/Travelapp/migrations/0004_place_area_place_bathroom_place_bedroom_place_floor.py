# Generated by Django 4.2.5 on 2023-10-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelapp', '0003_rename_des_place_address_rename_name_place_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='Area',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='Bathroom',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='Bedroom',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='Floor',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
