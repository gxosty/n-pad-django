from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    author             = models.ForeignKey(User, on_delete = models.CASCADE)
    note_title         = models.CharField(verbose_name = "Note Title", max_length = 64)
    note_content       = models.TextField()
    note_date          = models.DateTimeField()
    note_last_modified = models.DateTimeField()

    verbose_name = "Note"
    verbose_name_plural = "Notes"

    def __str__(self):
        return self.author.username + " | " + self.note_title

    def modified(self):
        self.note_last_modified = timezone.now()