from django.urls import path
from .views import IndexView, Postview,DodajPostView, EdytujPostView, UsunPostView, post_detail
from . import views
urlpatterns = [
    # path('', views.post_list, name='index'),
    # path('post/<int:pk>', Postview.as_view(), name='post-widok'),
    path('dodaj_post/',DodajPostView.as_view(), name='dodaj_post'),
    path('edytuj_post/<int:pk>',EdytujPostView.as_view(), name='edytuj_post'),
    path('usun_post/<int:pk>/delete',UsunPostView.as_view(), name='usun_post'),
    # path('post/<int:pk>/dodaj_komentarz/',DodajKomnetarzView.as_view(), name='dodaj_komentarz'),
    path('search/',views.searchPost, name='searchPosts'),
    path('post/<int:id>',views.post_detail, name='post_detail'),
    path('',IndexView.as_view(),name='index'),
]
