from django.views.generic.detail import DetailView
from django.core.cache import cache
from part1.models import Song

class CachedDetailView(DetailView):

    def get_queryset(self):
        return super(CachedDetailView, self).get_queryset().select_related()

    def get_object(self, queryset=None):
        obj = cache.get('%s-%s' % (self.model.__name__.lower(), self.kwargs['pk']), None)

        if not obj:
            obj = super(CachedDetailView, self).get_object(queryset)
	        cache.set('%s-%s' % (self.model.__name__.lower(), self.kwargs['pk']), obj)

        return obj    

class SongDetail(CachedDetailView):
    model = Song
    template_name = 'song_detail.html'
