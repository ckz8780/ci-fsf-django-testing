from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'todo_list.html')
        
    def test_get_add_item_page(self):
        page = self.client.get('/add/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')
        
    def test_get_edit_item_page(self):
        # First create an item and save it into the test database
        item = Item(name='Create a Test')
        item.save()
        
        # Then use it to run the test
        page = self.client.get('/edit/{}/'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        # This time all we do is send through a known bad item ID (or bacon, because bacon is delicious)
        page = self.client.get('/edit/{}/'.format('bacon'))
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_item(self):
        response = self.client.post("/add/", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        item_id = item.id

        response = self.client.post("/edit/{}/".format(item_id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=item_id)

        self.assertEqual("A different name", item.name)
    
    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        item_id = item.id

        response = self.client.post("/toggle/{}/".format(item_id))

        item = get_object_or_404(Item, pk=item_id)
        self.assertEqual(item.done, True)