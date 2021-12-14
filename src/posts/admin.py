from django.contrib import admin

from posts.models import BlogPost


# Affichage du model BlogPost dans l'interface d'administration
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title", "published", "created_on", "last_updated",  # Champs afficher
    )
    list_editable = ("published", )  # Champ editable


admin.site.register(BlogPost, BlogPostAdmin)