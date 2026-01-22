mode: 'agent'
model: GPT-4.1

# Django App Updates

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory
- Update `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, and `admin.py` to support users, teams, activities, leaderboard, and workouts collections.
- Ensure `/` points to the api and `api_root` is present in `urls.py`.
