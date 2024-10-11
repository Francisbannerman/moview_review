from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import MovieReview
from .serializer import ReviewSerializer
from .permissions import IsAuthorOrReadOnly

class ReviewList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = MovieReview.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,IsAuthorOrReadOnly)
    authentication_classes = [JWTAuthentication]
    queryset = MovieReview.objects.all()
    serializer_class = ReviewSerializer