from django.db import models
from accounts.models import Account

# Create your models here.
class BaseClass(models.Model):
    state = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateField(auto_now=True)
    uc = models.ForeignKey(
        Account, default=None, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract=True
