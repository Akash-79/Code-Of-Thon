from django.contrib import admin
from .models import *

admin.site.register(authors)
admin.site.register(topics)
admin.site.register(collections)
admin.site.register(quotes)

