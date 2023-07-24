from django.db import models

class Equipamentos(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.name