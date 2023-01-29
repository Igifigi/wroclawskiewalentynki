# wroclawskiewalentynki

Run on Windows:
1) Create `localsettings.py` in `wroclawskiewalentynki` directory and set 'DEBUG', 'SECRET_KEY', 'EMAIL_BACKEND', 'EMAIL_HOST', 'EMAIL_FROM', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'EMAIL_PORT' AND 'NOREPLY_EMAIL'
2) `python -m venv env`
3) `env\Scripts\Activate.ps1` (for PowerShell)
4) `pip install -r requirments.txt`
5) `python manage.py migrate`
6) `python manage.py runserver`

Run on Linux, Mac Os
1) Create `localsettings.py` in `wroclawskiewalentynki` directory and set 'DEBUG', 'SECRET_KEY', 'EMAIL_BACKEND', 'EMAIL_HOST', 'EMAIL_FROM', 'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'EMAIL_PORT' AND 'NOREPLY_EMAIL'
2) `python3 -m venv env`
3) `source env/bin/activate`
4) `pip install -r requirments.txt`
5) `python3 manage.py migrate`
6) `python3 manage.py runserver`
