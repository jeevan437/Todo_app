from django.db import models

# Create your models here.

status_choices = (
                    ('PARKED ','parked'),
                    ('STARTED','started'),
                    ('FINISHED','finished')
                )
class todo(models.Model):

    task_name = models.CharField(max_length=100, unique=True)
    task_description = models.TextField()
    task_status = models.CharField(max_length=50,choices=status_choices)

    def __str__(self):
        return self.task_name