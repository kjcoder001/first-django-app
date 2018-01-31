from django.db import models

# Create your models here.
class conjecture_model(models.Model):
    number=models.IntegerField()
    output_list=models.TextField()
    
    def __str__(self):
        return str(self.number)
