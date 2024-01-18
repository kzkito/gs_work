from django.contrib import admin
from .models import UserRequest, TranslationResponse

admin.site.register(UserRequest)
admin.site.register(TranslationResponse)
