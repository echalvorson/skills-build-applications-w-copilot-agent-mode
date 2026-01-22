from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly for test data setup
        db = connection.cursor().db_conn.client['octofit_db']
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_workout'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_leaderboard'].drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard')
        workout2 = Workout.objects.create(name='Speed Run', description='Speed and agility training', difficulty='Medium')
        workout3 = Workout.objects.create(name='Flight School', description='Aerial maneuvers', difficulty='Easy')

        # Create Users (Superheroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], workout=workout1, date=timezone.now().date(), duration_minutes=60, calories_burned=500)
        Activity.objects.create(user=users[1], workout=workout2, date=timezone.now().date(), duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workout3, date=timezone.now().date(), duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=users[3], workout=workout1, date=timezone.now().date(), duration_minutes=50, calories_burned=450)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=900, week=3, year=2026)
        Leaderboard.objects.create(team=dc, total_points=750, week=3, year=2026)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
