
from django.db import models
from django.utils import timezone


# Create your models here.

class FilePost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject_file = models.ForeignKey('SubjectFiles', on_delete=models.CASCADE, related_name='subject_file_post')
    tittle = models.CharField(max_length=140)
    file = models.FileField()
    description_file_post = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.tittle

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class SubjectFiles(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject_files = models.CharField(max_length=140)
    description_subject = models.TextField()

    def __str__(self):
        return self.subject_files
