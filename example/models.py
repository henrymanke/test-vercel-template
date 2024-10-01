from django.db import models

class TestFileUpload(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title
