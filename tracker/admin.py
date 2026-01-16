from django.contrib import admin
from .models import Profile, Activity

admin.site.register(Profile)


class ActivityAdmin(admin.ModelAdmin):
    # This tells Django which columns to show in the list view
    list_display = ('title', 'user', 'category', 'xp_amount', 'date_completed')

    # This adds a filter sidebar so you can sort by category
    list_filter = ('category', 'user')


# Register the new settings
admin.site.register(Activity, ActivityAdmin)
