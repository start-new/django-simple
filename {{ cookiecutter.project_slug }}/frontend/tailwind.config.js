/** @type {import('tailwindcss').Config} */

const Path = require("path");
const pwd = process.env.PWD;

const projectPaths = [
  Path.join(pwd, "../{{ cookiecutter.project_slug }}/templates/**/*.html"),
  Path.join(pwd, "../{{ cookiecutter.project_slug }}/templates/**/*.py"),
  Path.join(pwd, "./src/**/*.js"),
];

const pythonPaths = [
  Path.join(pwd, "../.venv/**/crispy_tailwind/**/*.html"),
  Path.join(pwd, "../.venv/**/crispy_tailwind/**/*.py"),
  Path.join(pwd, "../.venv/**/crispy_tailwind/**/*.js"),
];

const contentPaths = [...projectPaths, ...pythonPaths];

console.log(`tailwindcss will scan ${contentPaths}`);

module.exports = {
  content: contentPaths
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
