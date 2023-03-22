from pathlib import Path
import random
import shutil
import secrets


def remove_frontend_folder():
    """Removes the frontend folder if webpack is not required."""
    shutil.rmtree("frontend")


def remove_dockercompose_file():
    """Removes the docker-compose file if postgresql is not required."""
    Path("docker-compose.yml").unlink()


def remove_bootstrap_files():
    """Removes the files used with bootstrap css."""
    Path("frontend/src/styles/_variables.scss").unlink()


def remove_tailwind_files():
    """Removes the files used by tailwind css."""
    Path("frontend/tailwind.config.js").unlink()


def set_flag(
    file_path, flag, length=64, value=None, formatted=None, *args, **kwargs
):
    if value is None:
        value = secrets.token_urlsafe(length)

    with file_path.open("r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def set_django_secret_key():
    django_secret_key = set_flag(
        Path(".env"),
        "!!!SET DJANGO_SECRET_KEY!!!",
        length=64,
    )
    return django_secret_key


def set_postgres_auto_port():
    postgres_auto_port = random.randint(15432, 65535)
    set_flag(
        Path(".env"),
        "!!!SET POSTGRESQL_AUTO_PORT!!!",
        value=str(postgres_auto_port),
    )
    set_flag(
        Path("docker-compose.yml"),
        "!!!SET POSTGRESQL_AUTO_PORT!!!",
        value=str(postgres_auto_port),
    )
    return postgres_auto_port


def set_flags():
    set_django_secret_key()
    set_postgres_auto_port()


def main():
    """Final touches to our project."""

    set_flags()

    if "{{ cookiecutter.postgresql_version }}".lower() not in (
        "latest",
        "15",
        "14",
        "13",
        "12",
    ):
        remove_dockercompose_file()

    if (
        "{{ cookiecutter.use_bootstrap }}".lower() != "y"
        and "{{ cookiecutter.use_tailwindcss }}".lower() != "y"
    ):
        remove_frontend_folder()

    if "{{ cookiecutter.use_bootstrap }}".lower() != "y":
        remove_bootstrap_files()

    if "{{ cookiecutter.use_tailwindcss }}".lower() != "y":
        remove_tailwind_files()

    # Create a folder for the venv
    Path(".venv").mkdir()


if __name__ == "__main__":
    main()
