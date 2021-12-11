from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import DO_NOTHING
from utils.models import AbstractAutoField
import pghistory
from expense_app.enums import CostCategoryType
from mess_app.models import MessEvent

@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class CostCategory(AbstractAutoField):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=CostCategoryType.choices, default=CostCategoryType.MANDATORY)

    class Meta:
        db_table = "cost_category"

@pghistory.track(
    pghistory.AfterInsert("after_insert"),
    pghistory.AfterUpdate("after_update"),
    pghistory.BeforeDelete("before_delete"),
    obj_fk=None,
)
class MessEventNCostCategoryNUserCost(AbstractAutoField):
    mess_event = models.ForeignKey(
        MessEvent,
        on_delete=DO_NOTHING,
        related_name="mess_event_id_on_mess_event_n_cost_category_n_user_cost" 
    )
    cost_category = models.ForeignKey(
        CostCategory,
        on_delete=DO_NOTHING,
        related_name="cost_category_id_on_mess_event_n_cost_category_n_user_cost" 
    )
    user = models.ForeignKey(
        User,
        on_delete=DO_NOTHING,
        related_name="user_id_on_mess_event_n_cost_category_n_user_cost"
    )
    description = models.CharField(max_length=200, null=True)
    cost = models.FloatField()

    class Meta:
        db_table = "mess_event_n_cost_category_user_cost"
