from django.contrib import admin
from .models import TestFileUpload

@admin.register(TestFileUpload)
class TestFileUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload')
