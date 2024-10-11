from django.urls import path

from .views import ReviewDetail, ReviewList

urlpatterns = [
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
    path("review/", ReviewList.as_view(), name="review_list"),
]