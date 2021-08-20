from django.contrib import admin
# import your models here
from .models import Bat, Feeding

# Register your models here
admin.site.register(Bat)
admin.site.register(Feeding)

