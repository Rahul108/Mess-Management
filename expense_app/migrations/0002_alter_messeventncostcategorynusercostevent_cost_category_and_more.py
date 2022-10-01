# Generated by Django 4.1 on 2022-08-25 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess_app', '0007_alter_messeventevent_mess_alter_messnuserevent_mess_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messeventncostcategorynusercostevent',
            name='cost_category',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cost_category_id_on_mess_event_n_cost_category_n_user_cost', to='expense_app.costcategory'),
        ),
        migrations.AlterField(
            model_name='messeventncostcategorynusercostevent',
            name='mess_event',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mess_event_id_on_mess_event_n_cost_category_n_user_cost', to='mess_app.messevent'),
        ),
        migrations.AlterField(
            model_name='messeventncostcategorynusercostevent',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_id_on_mess_event_n_cost_category_n_user_cost', to=settings.AUTH_USER_MODEL),
        ),
    ]
