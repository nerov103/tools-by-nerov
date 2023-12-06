from django.contrib import admin
from .models import Tabel
# Register your models here.
@admin.register(Tabel)
class TableAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    