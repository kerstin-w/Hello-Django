from django.test import TestCase
from .models import Item


class TestModals(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertFalse(item.done)
