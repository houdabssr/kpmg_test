from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Ticket(models.Model):
    intitulé = models.CharField(max_length=266)
    description = models.TextField()
    date = models.DateField(default=now)
    info = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

# pour mieux reconnaître les objets
    def __str__(self):
        return self.intitulé

    class Meta:
        ordering = ['-date']

class Intitulé(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

#     class Meta:
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name