from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    favorite_set = GenericRelation(Favorite)
    objects = SongManager()

    def __unicode__(self):
        return u'%s - %s' % (self.artist, self.title)
    
    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)
        cache.delete('song-%s' % self.pk)
