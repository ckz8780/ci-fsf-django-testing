from django.test import TestCase
from .models import Item

class TestItemModel(TestCase):

    def test_done_defaults_to_false(self):
        # First create/ssave the item in the test DB
        item = Item(name="Create a Test")
        item.save()
        
        # Now let's check that we have the right item, and that its 'done' property is false
        self.assertEqual(item.name, "Create a Test")
        self.assertFalse(item.done)
    
    def test_can_create_an_item_with_a_name_and_status(self):
        # First create/ssave the item in the test DB
        item = Item(name="Create a Test", done=True)
        item.save()
        
        # Now test its props for correctness
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Item(name='Create a Test')
        self.assertEqual('Create a Test', str(item))