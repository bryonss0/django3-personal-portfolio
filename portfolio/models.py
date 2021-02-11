from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) #models.get_absolute_url

    def __str__(self):     # insteaed of Project object(1)
        return self.title  # returns title of Project
                           # like My First Portfolio
