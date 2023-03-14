/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../{{ cookiecutter.project_slug }}/templates/**/*.html",
    "../{{ cookiecutter.project_slug }}/templates/**/*.py",
    "./src/**/*.js",
    "../.venv/**/crispy_tailwind/**/*.html",
    "../.venv/**/crispy_tailwind/**/*.py",
    "../.venv/**/crispy_tailwind/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
