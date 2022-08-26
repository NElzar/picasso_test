import csv
from accident.models import Call
from datetime import datetime
from django.core.management.base import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Script to save data'

    def handle(self, *args, **options):
        count = 0
        start_time = datetime.now()
        Call.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Opening file….'))
        with open('police-department-calls-for-service.csv', newline='') as csvfile:
            reader = list(csv.DictReader(csvfile))
            self.stdout.write(self.style.SUCCESS('Started'))
            pbar = tqdm(total=len(reader))
            for row in reader:
                obj, created = Call.objects.get_or_create(
                    crime_id=row['Crime Id'],
                    defaults=dict(
                        original_crime_type_name=row['Original Crime Type Name'],
                        report_date=row['Report Date'],
                        call_date=row['Call Date'],
                        offense_date=row['Offense Date'],
                        call_time=row['Call Time'],
                        call_date_time=row['Call Date Time'],
                        disposition=row['Disposition'],
                        address=row['Address'],
                        city=row['City'],
                        state=row['State'],
                        agency_id=row['Agency Id'],
                        address_type=row['Address Type'],
                        common_location=row['Common Location']))
                if created:
                    count += 1
                pbar.update(1)
                if count == 100:
                    break
        end_time = datetime.now() - start_time
        total_count = Call.objects.count()
        self.stdout.write(self.style.SUCCESS('Finish'))
        self.stdout.write(self.style.SUCCESS(f'Spend time: {end_time}'))
        self.stdout.write(self.style.SUCCESS(f'Created: {count}'))
        self.stdout.write(self.style.SUCCESS(f'All created in DB: {total_count}'))
