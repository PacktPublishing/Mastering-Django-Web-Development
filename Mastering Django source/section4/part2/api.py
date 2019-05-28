from tastypie.resources import ModelResource
from part1.models import Artist, Album, Song
from tastypie import fields
from tastypie.api import Api
from tastypie.exceptions import InvalidFilterError
import datetime


class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artist'

class AlbumResource(ModelResource):
    artist = fields.ForeignKey(ArtistResource, 'artist')

    class Meta:
        queryset = Album.objects.all()
        resource_name = 'album'

    def dehydrate(self, bundle):
        bundle.data['year'] = bundle.obj.year
        return bundle

    def build_filters(self, filters=None):
        res = super(AlbumResource, self).build_filters(filters)

        if 'year' in filters:
            try:
                res.update({'year': int(filters['year'])})
            except:
                raise InvalidFilterError('year must be an integer!')
        return res

    def apply_filters(self, request, applicable_filters):
        year = applicable_filters.pop('year', None)
        qs = super(AlbumResource, self).apply_filters(request, applicable_filters)

        if year is not None:
            return qs.filter(
                release_date__gte=datetime.date(year,1,1), 
                release_date__lte=datetime.date(year,12,31))
        return qs


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
