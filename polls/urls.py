from django.urls import path, include

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.index, name='home'),
    path("<int:pk>", views.detailpage, name="results"),
    path("<int:pk>/results/", views.results, name="vote"),
    path("<int:question_id>/vote", views.vote, name="vote"),

    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
