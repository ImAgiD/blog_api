from django.contrib import admin

from .models import User

class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', )
    search_fields = ('email', )

admin.site.register(User, AccountAdmin)



