from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .forms import *
from .models import *
from .serializers import *

# Create your views here. (DJANGO)

class home(TemplateView):
    template_name = "index.html"

class income(TemplateView):
    template_name = "income.html"
    form_class = incomeForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        data = Income.objects.all()
        context = {'form1':form, "data1":data}
        return context

    def post(self, request):
        form = incomeForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/income')

class expense(TemplateView):
    template_name = "expense.html"
    form_class = expenseForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class
        data = Expense.objects.all()
        context = {'form2':form, "data2":data}
        return context

    def post(self, request):
        form = expenseForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/expense')

# REST Views
class incomeView(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = incomeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['personName','enteredAmount',]

class expenseView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = expenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['personName', 'category', 'expenseAmount',]