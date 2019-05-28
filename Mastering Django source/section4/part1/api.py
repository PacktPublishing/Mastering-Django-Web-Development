from tastypie.resources import ModelResource
from part1.models import Artist, Album, Song
from tastypie import fields
from tastypie.api import Api


class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artist'

class AlbumResource(ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')

    class Meta:
        queryset = Album.objects.all()
        resource_name = 'album'


class SongResource(ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')
    album = fields.ForeignKey(AlbumResource, 'album')

    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'

v1_api = Api(api_name='v1')
v1_api.register(ArtistResource())
v1_api.register(AlbumResource())
v1_api.register(SongResource())
