# Generated by Django 3.1.2 on 2023-04-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20230418_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
