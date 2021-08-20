from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Income(models.Model):
    personName = models.CharField(max_length=10)
    enteredAmount = models.FloatField()

    def __str__(self):
        return self.personName

class Expense(models.Model):
    personName = models.ForeignKey(Income, on_delete=CASCADE)
    category = models.CharField(max_length=20)
    expenseAmount = models.FloatField()

    # def remaining(self):
    #     expense = self.expenseAmount
    #     income = Income.enteredAmount

    #     left = income - expense

    #     return left

    def __str__(self) -> str:
        return self.category