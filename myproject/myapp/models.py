from django.db import models

class Content(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200, blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.text
