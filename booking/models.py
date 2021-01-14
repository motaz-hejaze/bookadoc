from django.db import models

# Create your models here.


class DocSession(models.Model):
    title = models.CharField(_('Title'), max_length=200, blank=False, null=False, required=True)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=10)
    date = models.DateField(_('Date'))
    start_time = models.TimeField(_('Start Time'), )
    end_time = models.TimeField(_('End Time'),)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)