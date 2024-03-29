# Generated by Django 3.1.7 on 2021-12-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pghistory', '0003_auto_20201023_1636'),
        ('mess_app', '0004_auto_20211211_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessEventEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pgh_id', models.AutoField(primary_key=True, serialize=False)),
                ('pgh_created_at', models.DateTimeField(auto_now_add=True)),
                ('pgh_label', models.TextField(help_text='The event label.')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('number_of_days', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('id', models.IntegerField()),
                ('mess', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='+', to='mess_app.mess')),
                ('pgh_context', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pghistory.context')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='messdurationevent',
            name='mess',
        ),
        migrations.RemoveField(
            model_name='messdurationevent',
            name='pgh_context',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='code',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='name',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='pgh_context',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='pgh_created_at',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='pgh_id',
        ),
        migrations.RemoveField(
            model_name='messevent',
            name='pgh_label',
        ),
        migrations.AddField(
            model_name='messevent',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messevent',
            name='mess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mess_id_on_mess_event', to='mess_app.mess'),
        ),
        migrations.AddField(
            model_name='messevent',
            name='number_of_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messevent',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='messevent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='messevent',
            table='mess_event',
        ),
        migrations.DeleteModel(
            name='MessDuration',
        ),
        migrations.DeleteModel(
            name='MessDurationEvent',
        ),
    ]
