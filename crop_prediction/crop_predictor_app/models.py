from django.db import models

# Create your models here.
class CropDetails(models.Model):
    name = models.CharField(max_length=200)
    nitrogen_content = models.IntegerField(default=0, null=True)
    phosphorus_content = models.IntegerField(default=0, null=True)
    potassium_content = models.IntegerField(default=0, null=True)
    temperature = models.IntegerField(default=0, null=True)
    humidity = models.IntegerField(default=0, null=True)
    ph = models.IntegerField(default=0, null=True)
    rainfall = models.IntegerField(default=0, null=True)
    
    def __str__(self):
        return f'{self.name}_{self.nitrogen_content}_{self.phosphorus_content}_{self.potassium_content}'
    
    