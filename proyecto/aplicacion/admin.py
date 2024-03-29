from django.contrib import admin
from .models import *

# Register your models here.

#class CursoAdmin(admin.ModelAdmin):
#    list_display = ("nombre", "comision")
#    list_filter = ("nombre",)


admin.site.register(PagoPendiente)
admin.site.register(Cliente)
admin.site.register(Cheques)
admin.site.register(User)