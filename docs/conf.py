# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Cache Invalidation Manager'
copyright = '2023, Thomas Pennant'
author = 'Thomas Pennant'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']