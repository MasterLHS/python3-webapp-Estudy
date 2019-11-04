from django.conf.urls import url

from .views import AddFavView, CommentView


urlpatterns = [
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
    url(r'^add_comment/$', CommentView.as_view(), name="add_comment"),
]
