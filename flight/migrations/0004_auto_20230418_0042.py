# Generated by Django 3.1.2 on 2023-04-17 19:12

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20230416_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='user',
            trigger=pgtrigger.compiler.Trigger(name='protect_deletes', sql=pgtrigger.compiler.UpsertTriggerSql(func="RAISE EXCEPTION 'pgtrigger: Cannot delete rows from % table', TG_TABLE_NAME;", hash='4cb594da4bda0730455436a172b2ad59ca7fcd69', operation='DELETE', pgid='pgtrigger_protect_deletes_9c1cc', table='flight_user', when='BEFORE')),
        ),
    ]
