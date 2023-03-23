from django.db import models

class Developer(models.Model)
    Developer_ID = models.Autofield(primary_key=True)
    Developer_Name = models.CharField(max_length=1000)
    Developer_Image = models.ImageField(upload_to='images/')
    Developer_Country = models. CharField(max_length=500)
    Developer_Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Developer_Name
