from django.db import models

class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'