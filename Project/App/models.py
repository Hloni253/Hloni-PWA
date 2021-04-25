from django.db import models
from django.urls import reverse


class AppModel(models.Model):
    app_name = models.CharField(max_length=50)

    def __str__(self):
        return self.app_name

    def get_app(self):
        return reverse("my app", kwargs={"id":self.id})
