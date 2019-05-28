from part1.models import Artist, Album
from django.db.models.manager import Manager
import datetime

class AlbumManager(Manager):
    def by_year(self, year):
        return self.get_queryset().filter(
            release_date__gte=datetime.date(year,1,1), 
            release_date__lte=datetime.date(year,12,31))

class SongManager(Manager):
    def by_year(self, year):
        return self.get_queryset().filter(
            album__release_date__gte=datetime.date(year,1,1), 
            album__release_date__lte=datetime.date(year,12,31))

    def rolling_7(self):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        return self.get_queryset().filter(
            album__release_date__gte=week_ago, 
            album__release_date__lte=today)








class NewSongManager(SongManager):
    def new_song(self, song_title, artist, album, release_date):
        artist = Artist.objects.get_or_create(name=artist)[0]
        album = Album.objects.get_or_create(
        	title=album, 
        	artist=artist, 
        	release_date=release_date
        	)[0]

        song = self.model(title=song_title, 
        	artist=artist, 
        	album=album)

        song.save(using=self._db)

        return song

# >>> Song.objects.new_song("The Song That Never Ends", "Lamb Chop", \ 
#     "Lamb Chop's Hits", today)
# >>> 
