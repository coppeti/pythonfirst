from django.urls import path

from posts.views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),  # si url est 'localhost > blog/', appel la vue BlogHome
    path('create/', BlogPostCreate.as_view(), name="create"),  # Appel le formulaire de création d'un article
    path('edit/<str:slug>/', BlogPostEdit.as_view(), name="edit"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),
]
