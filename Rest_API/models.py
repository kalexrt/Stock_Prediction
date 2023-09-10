from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class DataStock(models.Model):
    SNo = models.IntegerField(_("SNo"))
    Symbol = models.CharField(_("Symbol"),max_length=50)
    Date = models.DateField(_("Date"), auto_now=True)
    Open = models.FloatField(_("Open"))
    High = models.FloatField(_("High"))
    Low = models.FloatField(_("Low"))
    Close = models.FloatField(_("Close"))
    Vol = models.FloatField(_("Vol"))


class Index(models.Model):
    nepse = models.FloatField()
    sensitive = models.FloatField()
    float = models.FloatField()
    sensitivefloat = models.FloatField()
    date = models.DateField()

