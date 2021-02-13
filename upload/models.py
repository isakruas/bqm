from django.db import models
import os
from time import strftime


def path(instance, filename):
    ext = filename.split('.')[-1]

    filename = "%s_%s_%s_%s_%s_%s.%s" % (
        strftime('%y'),
        strftime('%m'),
        strftime('%d'),
        strftime('%H'),
        strftime('%M'),
        strftime('%S'),
        ext
    )

    return os.path.join('uploads', filename)


class Base(models.Model):
    class Meta:
        abstract = True


class Upload(Base):

    upload = models.FileField(upload_to=path, max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'

    def __str__(self):
        return self.upload
