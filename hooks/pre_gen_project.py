import sys

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert (
        project_slug.isidentifier()
    ), f"'{project_slug}' project slug is not a valid Python identifier."

assert (
    project_slug == project_slug.lower()
), f"'{project_slug}' project slug should be all lowercase"


if (
    "{{ cookiecutter.use_bootstrap }}" == "y"
    and "{{ cookiecutter.use_tailwindcss }}" == "y"
):
    print("You should not use Bootstrap and Tailwindcss " "at the same time.")
    sys.exit(1)
