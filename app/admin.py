from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)

admin.site.site_header = "Budget App Administartion"