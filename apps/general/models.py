from django.db import models

# Create your models here.

class General(models.Model):
    online = models.BooleanField(default=True)
