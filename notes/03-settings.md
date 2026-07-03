# Django Settings

`settings.py` is the main configuration file of a Django project.

---

## BASE_DIR

```python
BASE_DIR = Path(__file__).resolve().parent.parent
```

Represents the project's root directory and is used to build file paths.

---

## Environment Variables

```python
load_dotenv()
os.getenv(...)
```

Used to load sensitive values from a `.env` file.

---

## INSTALLED_APPS

Registers all active applications in the project.

Usually divided into:

* Django apps
* Third-party apps
* Local apps

---

## DATABASES

Configures the project's database.

`dj_database_url` converts a database URL into Django's database configuration.

---

## AUTH_PASSWORD_VALIDATORS

Defines password validation rules (minimum length, common passwords, etc.).

---

## Internationalization

```python
LANGUAGE_CODE
TIME_ZONE
USE_I18N
USE_TZ
```

Controls the project's language and timezone settings.

---

## Static & Media

* **Static:** Project files (CSS, JS, Images).
* **Media:** User uploaded files.

---

## Authentication

```python
LOGIN_URL
LOGIN_REDIRECT_URL
LOGOUT_REDIRECT_URL
```

Defines login and logout redirect behavior.

---

## CSRF_TRUSTED_ORIGINS

Defines trusted domains that are allowed to send authenticated requests.

---

## Production Storage

When `DEBUG=False`, uploaded files can be stored in cloud storage instead of the local filesystem.
