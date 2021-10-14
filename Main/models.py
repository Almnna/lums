from django.db import models

# Create your models here.
class Lectures(models.Model):
    course = models.CharField(max_length=50)
    lecture_no = models.PositiveIntegerField()
    lecture_na = models.CharField(max_length=100)
    pdf = models.CharField(max_length=100)
    ppt = models.CharField(max_length=100)
    word = models.CharField(max_length=100, default="0")
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.course + " | " + self.lecture_na + " " + str(self.lecture_no)