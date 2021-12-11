from django.db import models
from django.utils.translation import gettext_lazy as _

class CostCategoryType(models.TextChoices):
    MANDATORY = "MANDATORY", _("Mandatory")
    OPTIONAL = "OPTIONAL", _("Optional")