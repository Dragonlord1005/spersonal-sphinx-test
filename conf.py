# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('cheese/'))

# -- Project information -----------------------------------------------------

project = 'Testing'
copyright = '2021, Dragonlord1005'
author = 'Dragonlord1005'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxext.opengraph', 'sphinx.ext.napoleon', 'sphinx_copybutton', 'sphinx_inline_tabs', 'sphinx.ext.duration', 'releases',
]
# 'myst_parser',

releases_issue_uri = "https://github.com/Dragonlord1005/personal-sphinx-test/issues/%s"
releases_release_uri = "https://github.com/Dragonlord1005/personal-sphinx-test/releases/%s"
# releases_release_uri = "https://github.com/Dragonlord1005/personal-sphinx-test/tree/%s"
releases_unstable_prehistory = True
releases_debug = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
opg_site_url = 'https://dragonlord1005.github.io/personal-sphinx-test'
source_suffix = {
    '.rst': 'restructuredtext',
}
