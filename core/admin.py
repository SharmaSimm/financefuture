from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender')  # Adjust fields as per your model
    search_fields = ['user__username']


