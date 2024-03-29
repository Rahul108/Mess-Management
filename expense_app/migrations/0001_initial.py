# Generated by Django 3.1.7 on 2021-12-11 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pghistory', '0003_auto_20201023_1636'),
        ('mess_app', '0005_auto_20211212_0022'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('MANDATORY', 'Mandatory'), ('OPTIONAL', 'Optional')], default='MANDATORY', max_length=200)),
            ],
            options={
                'db_table': 'cost_category',
            },
        ),
        migrations.CreateModel(
            name='MessEventNCostCategoryNUserCostEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pgh_id', models.AutoField(primary_key=True, serialize=False)),
                ('pgh_created_at', models.DateTimeField(auto_now_add=True)),
                ('pgh_label', models.TextField(help_text='The event label.')),
                ('description', models.CharField(max_length=200, null=True)),
                ('cost', models.FloatField()),
                ('id', models.IntegerField()),
                ('cost_category', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='+', to='expense_app.costcategory')),
                ('mess_event', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='+', to='mess_app.messevent')),
                ('pgh_context', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pghistory.context')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessEventNCostCategoryNUserCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('cost', models.FloatField()),
                ('cost_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_category_id_on_mess_event_n_cost_category_n_user_cost', to='expense_app.costcategory')),
                ('mess_event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mess_event_id_on_mess_event_n_cost_category_n_user_cost', to='mess_app.messevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_id_on_mess_event_n_cost_category_n_user_cost', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mess_event_n_cost_category_user_cost',
            },
        ),
        migrations.CreateModel(
            name='CostCategoryEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pgh_id', models.AutoField(primary_key=True, serialize=False)),
                ('pgh_created_at', models.DateTimeField(auto_now_add=True)),
                ('pgh_label', models.TextField(help_text='The event label.')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('MANDATORY', 'Mandatory'), ('OPTIONAL', 'Optional')], default='MANDATORY', max_length=200)),
                ('id', models.IntegerField()),
                ('pgh_context', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pghistory.context')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
