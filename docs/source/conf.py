# Originaly from Juan Luis Cano Rodríguez
# https://www.youtube.com/watch?v=qRSb299awB0&t=1700s
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pathlib import Path

project = "extra-streamlit-tools"
copyright = "2022, Tomer Gabay"
author = "Tomer Gabay"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "nbsphinx",
]
autoapi_type = "python"
autoapi_dirs = [f"{Path(__file__).parents[2]}/src"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def should_skip_member(app, what, name, obj, skip, options):
    exclude_modules = ["extra_streamlit_tools._logging"]
    return name in exclude_modules


def setup(app):
    app.connect("autodoc-skip-member", should_skip_member)
