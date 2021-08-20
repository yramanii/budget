from django.test import TestCase
from django.test.client import Client
from django.urls.base import reverse

from .models import *

# Create your tests here.
class Test(TestCase):


    def setUp(self):
        
        # for model
        Income.objects.create(
            personName="yash",
            enteredAmount=5000
        )

        # for views
        self.client = Client()
        self.expense_url = reverse("expense")



    # for model
    def test1(self):

        obj1 = Income.objects.get(
            personName="yash",
            enteredAmount=5000
        )

        self.assertEqual(obj1.personName, "yash")
        self.assertEqual(obj1.enteredAmount, 5000)

    

    # for views
    def test_expense(self):
        response = self.client.get(self.expense_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "expense.html")