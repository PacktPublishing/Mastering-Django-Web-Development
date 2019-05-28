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
