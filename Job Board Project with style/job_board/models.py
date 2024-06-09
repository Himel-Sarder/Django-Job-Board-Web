from django.db import models

# Create your models here.
#job posting tables
class JobPosting(models.Model):
    # title, description, company, salary, location
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

