from django.contrib import admin

# modele musimy zaimportować
from .models import Category, Location, Employee, Device

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Employee)
admin.site.register(Device)