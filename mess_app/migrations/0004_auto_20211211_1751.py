# Generated by Django 3.1.7 on 2021-12-11 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pghistory', '0003_auto_20201023_1636'),
        ('mess_app', '0003_messdurationdata_messdurationdataevent_messnduration_messndurationevent_messnuser_messnuserevent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MessNDuration',
            new_name='MessDuration',
        ),
        migrations.RenameModel(
            old_name='MessNDurationEvent',
            new_name='MessDurationEvent',
        ),
        migrations.RemoveField(
            model_name='messdurationdataevent',
            name='mess_n_duration',
        ),
        migrations.RemoveField(
            model_name='messdurationdataevent',
            name='pgh_context',
        ),
        migrations.DeleteModel(
            name='MessDurationData',
        ),
        migrations.DeleteModel(
            name='MessDurationDataEvent',
        ),
    ]
