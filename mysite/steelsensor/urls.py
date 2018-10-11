from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name='index'),
	path("results", views.results, name='results'),
	path("browse", views.browse, name='browse'),
	path("dbcreate", views.dbcreate, name='dbcreate'),
	path("dbdelete", views.dbdelete, name='dbdelete'),
	path("deleteImages", views.deleteImages, name='deleteImages'),
	path("browsematches", views.browsematches, name='browsematches'),
	path("admintools", views.admintools, name='admintools')
]
