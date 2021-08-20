from django.urls import path,include

from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register("income", incomeView)
router.register("expense", expenseView)

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('income/', income.as_view(), name="income"),
    path('expense/', expense.as_view(), name="expense"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]