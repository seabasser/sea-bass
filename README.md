# CBaaS (Cheap Booze as a Service)

You've arrived at the repo for the backend for the CBaaS service.

## Getting Started

This project uses pipenv to manage its dependencies.
[pyenv](https://github.com/pyenv/pyenv) to install/manage the appropriate python (currently 3.9.x), pip 
and pipenv version. Once you have pipenv, do the following:

```bash
pipenv install --dev
```

Afterwards you can run the server by running the following:

```bash
pipenv run serve
```

By default, the server is configured to listen on all interfaces on port 5000.

## Run Tests

You can run flake8 and pytests by running:

```bash
pipenv run pytest
pipenv run flake8
```

Arguments are accepted in the above commands when needed. Example: `--disable-pytest-warnings`
