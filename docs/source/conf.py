# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ASC treebank project'
copyright = 'will be edited'
author = 'will be added'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'recommonmark',
    'sphinx.ext.viewcode'
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']


