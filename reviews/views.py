from django.shortcuts import render
from rest_framework import generics

from .models import MovieReview
from .serializer import ReviewSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = ReviewSerializer