from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth import get_user_model

# User = get_user_model()

class MovieReview(models.Model):
    movie_title = models.CharField(max_length=255)
    review_content = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_title
