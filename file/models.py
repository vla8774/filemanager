from django.db import models
from django.utils import timezone
import transliterate
from django.contrib.auth.models import User

# Create your models here.
from transliterate import translit


class SubjectFiles(models.Model):
    subject_files = models.CharField(max_length=140)
    description_subject = models.TextField()
    slug = models.SlugField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        slug = translit(self.subject_files, 'ru', reversed=True)
        self.slug = slug.replace(" ", "_")
        super(SubjectFiles, self).save(*args, **kwargs)


class Phone(models.Model):
    published_date = models.DateTimeField(
        blank=True, null=True)
    file = models.FileField(blank=True, null=True, )


class FilePost(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    subject_file = models.ForeignKey(SubjectFiles, on_delete=models.CASCADE, related_name='subject_file_post')
    slug = models.SlugField(max_length=140, blank=True, null=True)
    file = models.FileField(blank=True, null=True,)
    description_file_post = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        slug = translit(self.title, 'ru', reversed=True)
        self.slug = slug.replace(" ", "_")
        super(FilePost, self).save(*args, **kwargs)



