from django.db import models
from django.contrib.auth.models import User

app_name = 'menu'

class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    input_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user.username if self.user else 'Anonymous'} at {self.timestamp}"

class TranslationResponse(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('ZH', 'Chinese'),
    ]

    request = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    translated_text = models.TextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_language_display()} response to {self.request.id} at {self.timestamp}"
