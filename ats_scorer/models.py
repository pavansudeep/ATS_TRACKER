from django.db import models
from django.conf import settings

class Application(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    ats_score = models.FloatField(null=True, blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} applied to {self.job.title} - Score: {self.ats_score}%"
