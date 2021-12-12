from django.db import models
from django.db.models.deletion import DO_NOTHING
from utils.models import AbstractAutoField
import pghistory
from django.contrib.auth.models import User

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
        related_name="mess_id_on_mess_n_user",
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
class MessEvent(AbstractAutoField):
    mess = models.ForeignKey(
        Mess,
        on_delete=DO_NOTHING,
        related_name="mess_id_on_mess_event",
        null=True
    )
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    number_of_days = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "mess_event"