from django.db import models


def image_save(instance, filename):
    ext = filename.split(".")[-1]
    if not ext:
        # default extension if not uploaded from a file
        ext = "jpg"
    return "test" + "/QS_" + str(instance.name) + "." + ext


class UserProfile(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to=image_save)
