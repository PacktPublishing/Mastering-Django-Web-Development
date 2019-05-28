from part1.models import Song, Album
from django.forms.models import modelformset_factory, inlineformset_factory
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404


class BulkSongs(FormView):
    form_class = modelformset_factory(Song, extra=5, fields=['title', 'artist', 'album'])
    template_name = 'song_form.html'

    def form_valid(self, formset):
        instances = len(formset.save())
        if instances > 0:
            messages.success(self.request, '%s songs have been updated.' % instances)

        return HttpResponseRedirect('/bulk_songs')

    def get_form_kwargs(self):
        kwargs = super(BulkSongs, self).get_form_kwargs()
        kwargs.update({'queryset':Song.objects.none()})
        
        return kwargs


class UpdateAlbum(FormView):
    form_class = inlineformset_factory(Album, Song, extra=5, exclude=[])
    template_name = 'song_form.html'

    def form_valid(self, formset):
        instances = len(formset.save())
        if instances > 0:
            messages.success(self.request, '%s songs have been updated.' % instances)

        return redirect('update_album', self.album_id)

    def get_form_kwargs(self):
        self.album_id = self.kwargs['album_id']
        self.album = get_object_or_404(Album, pk=self.album_id)
        kwargs = super(UpdateAlbum, self).get_form_kwargs()
        kwargs.update({'instance':self.album})
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(UpdateAlbum, self).get_context_data(**kwargs)
        ctx.update({'col3':'Delete?'})
        return ctx
