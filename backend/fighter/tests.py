# FILEPATH: /root/wisiweb3tem/backend/fighter/tests.py
from django.test import TestCase
from .models import Fighter

class FighterModelTest(TestCase):
    def test_weight_choices(self):
        expected_choices = (
            ('SUPER_HEAVY', 'Super Heavy'),
            ('HEAVY', 'Heavy'),
            # ... rest of your choices here ...
            ('ATOM', 'Atom'),
            ('OTHER', 'Other'),
        )
        self.assertEqual(Fighter.WEIGHT_CHOICES, expected_choices)

    def test_champion_choices(self):
        expected_choices = (
            ('UFC', 'UFC'),
            ('MMA', 'MMA'),
            # ... rest of your choices here ...
            ('KARATE', 'Karate'),
            ('OTHER', 'Other'),
            ('NOT_HAVE', 'Not Have'),
        )
        self.assertEqual(Fighter.CHAMPION_CHOICES, expected_choices)

    def test_sport_c_choices(self):
        expected_choices = (
            ('UFC', 'UFC'),
            ('MMA', 'MMA'),
            # ... rest of your choices here ...
            ('KARATE', 'Karate'),
            ('OTHER', 'Other'),
        )
        self.assertEqual(Fighter.SPORT_C, expected_choices)

    def test_title_choices(self):
        expected_choices = (
            ('NOT_HAVE', 'Not Have'),
            ('M  |UFC', 'M | UFC'),
            # ... rest of your choices here ...
            ('M|WBC Interi M World', 'M | WBC Interi M World'),
            ('f|WBC Interi M World', 'f | WBC Interi M World'),
        )
        self.assertEqual(Fighter.TITLE_CHOICES, expected_choices)