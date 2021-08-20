from django.contrib import admin
# import your models here
from .models import Bat, Feeding, Relic

# Register your models here
admin.site.register(Bat)
admin.site.register(Feeding)
admin.site.register(Relic)
