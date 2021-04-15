from django.contrib import admin
from blog.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')


admin.site.register(Publication, PublicationAdmin)
