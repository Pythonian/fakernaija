"""Sphinx doc configurations."""

project = "Fakernaija"
copyright = "2024, Seyi Pythonian"
author = "Seyi Pythonian"
release = "1.0.0"

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]