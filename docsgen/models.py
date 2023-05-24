from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='templates')
    latex_text = models.TextField()

    def __str__(self):
        return self.name