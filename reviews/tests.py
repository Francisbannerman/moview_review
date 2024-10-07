from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import MovieReview

class ReviewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            email="test@tee.com",
            password="testpass"
        )

        cls.review = MovieReview.objects.create(
            movie_title="Adams Apples",
            review_content="The Apples of Adam are nice",
            rating=4,
            user_id=cls.user 
        )
    
    def test_review_model(self):
        self.assertEqual(self.review.movie_title, "Adams Apples")
        self.assertIn("Adam", self.review.review_content)
        self.assertEqual(self.review.review_content, "The Apples of Adam are nice")
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.user_id.email, "test@tee.com")

