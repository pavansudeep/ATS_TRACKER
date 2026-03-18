from django.db import models

class Job(models.Model):
    CATEGORY_CHOICES = (
        ('IT', 'IT'),
        ('NON-IT', 'Non-IT'),
    )
    
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    city = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField(help_text="Comma separated skills, e.g., Python, Django, SQL")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def skills_list(self):
        return [skill.strip() for skill in self.skills_required.split(',') if skill.strip()]

    def __str__(self):
        return f"{self.title} ({self.city})"
