from django.db import models

class Post(models.Model): #NEW
    text = models.TextField()

    def __str__(self): #NEW
        return self.text[:50]