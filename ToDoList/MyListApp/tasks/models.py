from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    
    class Meta:
        ordering = ["-date_added"]
    def __str__(self):
        return self.title
