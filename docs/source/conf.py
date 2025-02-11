"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys

# -- Path setup ----------------------------------------------------------------
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../examples"))

from qutree import __author__, __version__  # noqa

# -- Project information -------------------------------------------------------
project = "qutree"
copyright = f"2022-{datetime.now().year}, {__author__}"
author = __author__
release = __version__

# -- General configuration -----------------------------------------------------
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinx_copybutton",
    # https://github.com/spatialaudio/nbsphinx/issues/687
    "IPython.sphinxext.ipython_console_highlighting",
]
templates_path = ["_templates"]
exclude_patterns = ["**.ipynb_checkpoints"]  # when working in a Jupyter env.


# -- Options for HTML output ---------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_context = {
    "default_mode": "light",
    "github_user": "alice4space",
    "github_repo": "qutree",
    "github_version": "main",
    "doc_path": "docs/source",
}

# -- Options for autosummary/autodoc output ------------------------------------
autosummary_generate = True
autoclass_content = "init"
autodoc_typehints = "description"

# -- Option for Napoleon styling of tuple output -------------------------------
napoleon_custom_sections = [("Returns", "params_style")]

# -- Options of the HTML theme -------------------------------------------------
html_theme_options = {
    "logo": {"text": project},
    "use_edit_page_button": True,
    "show_prev_next": True,
    "navbar_end": ["navbar-icon-links"],  # remove theme change
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/alice4space/qutree",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org",
            "icon": "fa-brands fa-python",
        },
    ],
}
