from django.db import models
from django.db.models.deletion import DO_NOTHING
from utils.models import *
import pghistory
from django.contrib.auth.models import User, Group



@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class Mess(AbstractAutoField):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "mess"


@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class MessNUser(AbstractAutoField):
    mess = models.ForeignKey(
        Mess,
        on_delete=DO_NOTHING,
        related_name="mess_id_on_mess_n_user" 
    )
    user= models.ForeignKey(
        User,
        on_delete=DO_NOTHING,
        related_name="user_id" 
    )
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "mess_n_user"
    

@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class  MessNDuration(AbstractAutoField):
    mess = models.ForeignKey(
        Mess,
        on_delete=DO_NOTHING,
        related_name="mess_id_on_mess_n_duration" 
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    number_of_days = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mess_n_duration"



@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class MessDurationData(AbstractAutoField):
    mess_n_duration = models.ForeignKey(
        MessNDuration,
        on_delete=DO_NOTHING,
        related_name="mess_n_duration_id_on_mess_duration_data" 
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    number_of_days = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "mess_duration_data"