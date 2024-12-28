from django.db import models

class Subscriber(models.Model):
  email = models.EmailField(unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.email
  
class Newsletter(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title
  