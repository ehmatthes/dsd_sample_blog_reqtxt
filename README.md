This is a sample Django project for the `django-simple-deploy`. The purpose of this project is to make it easy for people to make trial runs of `django-simple-deploy`, with nothing more than a `git clone` command to get started.

For more information, see the [Contributing](https://django-simple-deploy.readthedocs.io/en/latest/contributing/) docs for `django-simple-deploy`.

## Updating requirements

To update requirements, run the update script and then run tests:

```sh
$ python update_requirements.py
$ uv pip install -r requirements.txt
$ python manage.py check
$ python manage.py runserver
$ python manage.py test_deployed_app_functionality.py --url http://localhost:8000/ --flush-db
$ git commit -am "Updated requirements."
```

This script works on macOS, and assumes `uv` is available.
