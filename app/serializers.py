from .models import *
from rest_framework import serializers

class incomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class expenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'