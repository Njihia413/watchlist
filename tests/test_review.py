import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    def setUp(self):
        self.new_review = Review(
            1234,
            'Python Must Be Crazy'
            'https://image.tmdb.org/t/p/w500/khsjha27hbs'
            'Awesome movie!!!'
        )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))