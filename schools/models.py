from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

PROVINCE_CHOICES = [
    ('North', 'North'),
    ('East', 'East'),
    ('West', 'West'),
    ('South', 'South'),
]

LEVEL_CHOICES = [
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Tertiary', 'Tertiary'),
]


class School(models.Model):
    name = models.CharField(_('School Name'), max_length=100, unique=True)
    province = models.CharField(
        _('School Province'), max_length=30, choices=PROVINCE_CHOICES)
    district = models.CharField(_('School District'), max_length=50)
    level = models.CharField(
        _('School Level'), max_length=30, choices=LEVEL_CHOICES)
    male = models.IntegerField(_('Male Students'), default=0)
    female = models.IntegerField(_('Female Students'), default=0)
    location = models.PointField(_('School Location'), srid=4326)
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Date Updated'), auto_now=False)


def __str__(self):
    return self.name


def get_school_first_name(self):
    return self.name.split()[0]


# Create your models here.
