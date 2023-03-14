{%- if cookiecutter.use_bootstrap == "y" -%}
module.exports = {
  plugins: [
    require("postcss-preset-env")
  ],
};
{%- elif cookiecutter.use_tailwindcss == "y" -%}
module.exports = {
  plugins: [
    require('postcss-import'),
    require('tailwindcss/nesting')('postcss-nesting'),
    require('tailwindcss'),
    require('postcss-preset-env')({
      features: { 'nesting-rules': false },
    })
  ]
}{% endif %}
