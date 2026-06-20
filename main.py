# main.py
import os
import sys
from pathlib import Path
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def simple_view(request):
    content = (
        "<h1>Hello from Django</h1>"
        "<p>A minimal Django website in one script.</p>"
        "<p>Visit /about for a second page.</p>"
    )
    return HttpResponse(content)

def about_view(request):
    return HttpResponse(
        "<h1>About</h1><p>This is a one-file Django example.</p>"
    )

urlpatterns = [
    path("", simple_view, name="home"),
    path("about/", about_view, name="about"),
]

def create_settings():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY="change-me-for-production",
            ROOT_URLCONF=__name__,
            ALLOWED_HOSTS=["*"],
            MIDDLEWARE=[
                "django.middleware.common.CommonMiddleware",
                "django.middleware.csrf.CsrfViewMiddleware",
                "django.middleware.clickjacking.XFrameOptionsMiddleware",
            ],
            INSTALLED_APPS=[
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
            ],
            TEMPLATES=[
                {
                    "BACKEND": "django.template.backends.django.DjangoTemplates",
                    "DIRS": [TEMPLATES_DIR],
                    "APP_DIRS": True,
                    "OPTIONS": {
                        "context_processors": [
                            "django.template.context_processors.debug",
                            "django.template.context_processors.request",
                            "django.contrib.messages.context_processors.messages",
                        ],
                    },
                }
            ],
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
                }
            },
            STATIC_URL="/static/",
        )

def create_template():
    if not os.path.isdir(TEMPLATES_DIR):
        os.makedirs(TEMPLATES_DIR, exist_ok=True)
    index_path = os.path.join(TEMPLATES_DIR, "index.html")
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as file:
            file.write(
                "<!DOCTYPE html>"
                "<html><head><title>Django One File</title></head>"
                "<body><h1>Welcome</h1><p>Generated template page.</p></body>"
                "</html>"
            )

def print_startup_message():
    print("Starting Django one-file website.")
    print("Open http://127.0.0.1:8000 in your browser.")
    print("Use Ctrl+C to stop the server.")

def main():
    create_settings()
    create_template()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)
    print_startup_message()
    argv = sys.argv[:]
    if len(argv) == 1:
        argv += ["runserver", "8000"]
    execute_from_command_line(argv)

if __name__ == "__main__":
    main()
