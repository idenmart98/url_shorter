from django.db import models
from django.urls import reverse



from .utils import generate_random_string


# Create your models here.

class Url(models.Model):
    origin_url = models.URLField(unique=True)
    short_code = models.CharField(unique=True,max_length=5)

    def save(self, *args, **kwargs):
        while True:
            random_str = generate_random_string()
            if not Url.objects.filter(short_code=random_str).exists():
                self.short_code = random_str
                break
            else:
                continue
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("redirect_origin_url", kwargs={"code": self.short_code})
    