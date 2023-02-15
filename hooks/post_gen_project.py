from pathlib import Path
import shutil
import secrets


def remove_frontend_folder():
    """Removes the frontend folder if webpack is not required."""
    shutil.rmtree("frontend")


def remove_dockercompose_file():
    """Removes the docker-compose file if postgresql is not required."""
    Path("docker-compose.yml").unlink()


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


def set_django_secret_key(file_path):
    django_secret_key = set_flag(
        file_path,
        "!!!SET DJANGO_SECRET_KEY!!!",
        length=64,
    )
    return django_secret_key


def set_flags():
    dotenv_path = Path(".env")
    set_django_secret_key(dotenv_path)


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

    if "{{ cookiecutter.use_webpack }}".lower() != "y":
        remove_frontend_folder()


if __name__ == '__main__':
    main()
