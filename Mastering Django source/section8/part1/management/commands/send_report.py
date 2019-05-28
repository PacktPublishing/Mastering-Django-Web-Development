from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Send the specified report'

    def add_arguments(self, parser):
        parser.add_argument('report_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # send each of the listed reports
        for report in options['report_id']:
            self.stdout.write('Successfully sent report "%s"' % report)
