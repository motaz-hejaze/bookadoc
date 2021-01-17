from django.db import models
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.


UserModel = get_user_model()


class DocSession(models.Model):
    SESSION_STATUS = (
        ('active','active'),
        ('inactive', 'inactive'),
        ('finished','finished'),
        ('cancelled','cancelled'),
    )
    SESSION_TYPE = (
        ('weekly','weekly'),
        ('one_day','one_day'),
    )
    title = models.CharField(_('Title'), max_length=200, blank=False, null=False)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=10 , blank=True, null=True)
    date = models.DateField(_('Date'), blank=False, null=False)
    start_time = models.TimeField(_('Start Time'), blank=False, null=False)
    end_time = models.TimeField(_('End Time'), blank=False, null=False)
    session_status = models.CharField(_('Session Status'), max_length=20, choices=SESSION_STATUS, default='active', blank=True, null=False)
    session_type = models.CharField(_('Session Type'), max_length=20, choices=SESSION_TYPE, blank=False, null=False)
    session_doctor = models.ForeignKey(UserModel , on_delete=models.CASCADE, blank=True, null=True,  related_name="doctor_sessions" )
    session_patient = models.OneToOneField(UserModel, on_delete=models.CASCADE, blank=False, null=False, related_name="patient_sessions")
    doctor_acceptance = models.BooleanField(_('Doctor Accepted'), default=False)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.session_doctor or self.session_doctor is None:
            self.session_status = 'inactive'
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-date',)
        verbose_name = 'Doctor Session'
        verbose_name_plural = 'Doctor Sessions'

    def __str__(self):
        return self.title