from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.models import BlogPost


# Class Based View - Affiche le model BlogPost complet (tous les articles)
class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    # Méthode pour empêcher l'affichage des articles non publiés si on est pas autentifié
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:  # Si user connecté
            return queryset  # retourne le model BlogPost si user logué

        return queryset.filter(published=True)  # Filter les article


# Class Based View - Affiche la page de création d'un article
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"  # Pour donner un nom specifique à notre template
    fields = ['title', 'content', ]  # Pour déterminer les champs que l'on peut renseigner


# Class Based View - Affiche un article afin de l'éditer
class BlogPostEdit(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published', ]


# Class Based View - Affichage d'un article en entier
class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"


# Class Based View - Suppression d'un article
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")