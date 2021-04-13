from django.contrib import admin
from blog.models import Author, Publication


class AuthorAdmin(admin.ModelAdmin):
    pass


class PublicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
