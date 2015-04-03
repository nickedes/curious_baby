from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /ques/
    url(r'^$', views.index, name='index'),
    # ex: /ques/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /ques/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /ques/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
