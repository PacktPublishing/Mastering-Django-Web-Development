from django.db import models
from part1.managers import AlbumManager, SongManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Artist(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return u'%s' % self.name

class Album(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    release_date = models.DateField()
    objects = AlbumManager()

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def year(self):
        return self.release_date.year

class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    objects = SongManager()

    def __unicode__(self):
        return u'%s - %s' % (self.artist, self.title)


class Favorite(models.Model):
    title = models.CharField(max_length=80)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        self.title = str(self.item)
        super(Favorite, self).save(*args, **kwargs)
