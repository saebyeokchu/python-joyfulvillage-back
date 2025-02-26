from django.utils.timezone import now
from django.db import models

# Create your models here.
class auth(models.Model) :
    eamilAddress = models.CharField(max_length=50)
    authCode = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)
    lastModifiedAt = models.DateTimeField(default=now)
