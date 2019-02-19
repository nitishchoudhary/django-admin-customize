from django.contrib import admin
from videos.models import Customer,Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    fields = ['release', 'name', 'duration']
    search_fields = ['name']
    list_filter = ['release', 'duration']
    list_display = ['release', 'duration', 'name']
    list_editable = ['duration']

admin.site.register(Customer)
admin.site.register(Movie, MovieAdmin)
