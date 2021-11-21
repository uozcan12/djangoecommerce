from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product

class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/fields attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

class TestProductsModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(category_id=1, title="django beginners", 
            created_by_id=1, slug="django-beginners", price="20.00", image="django")
