from django.conf.urls import patterns, include, url
from django.contrib import admin
from part1 import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^bulk_songs/', views.BulkSongs.as_view()),
	url(r'^update_album/(?P<album_id>\d+)/', views.UpdateAlbum.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
