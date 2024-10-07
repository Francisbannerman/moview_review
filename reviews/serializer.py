from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import CustomUser
from .models import MovieReview

User = CustomUser()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = (
            "id", "movie_title", "review_content", "rating", "user_id", "created_at", "updated_at"
        )