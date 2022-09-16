import datetime

import yaml

import intake_esm

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'myst_nb',
    'sphinxext.opengraph',
    'sphinx_copybutton',
    'sphinxcontrib.autodoc_pydantic',
    'sphinx_design',
]


# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

autodoc_pydantic_model_show_json = True
autodoc_pydantic_model_show_config = False

nb_execution_mode = 'cache'
nb_execution_timeout = 600
nb_execution_raise_on_error = True

extlinks = {
    'issue': ('https://github.com/intake/intake-esm/issues/%s', 'GH#'),
    'pr': ('https://github.com/intake/intake-esm/pull/%s', 'GH#'),
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []
autodoc_typehints = 'none'
autodoc_member_order = 'groupwise'

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True


# The suffix of source filenames.
# source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = 'Intake-ESM'
copyright = f'2018-{current_year}, Intake-ESM development team'
author = 'Intake-ESM developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = intake_esm.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = intake_esm.__version__


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = ''


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../_static/images/NSF_4-Color_bitmap_Logo.png'
html_context = {
    'github_user': 'intake',
    'github_repo': 'intake-esm',
    'github_version': 'main',
    'doc_path': 'docs',
}
html_theme_options = {}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Sometimes the savefig directory doesn't exist and needs to be created
# https://github.com/ipython/ipython/issues/8733
# becomes obsolete when we can pin ipython>=5.2; see ci/requirements/doc.yml


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'


# Output file base name for HTML help builder.
htmlhelp_basename = 'intake_esmdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}


latex_documents = [('index', 'intake-esm.tex', 'intake-esm Documentation', author, 'manual')]

man_pages = [('index', 'intake-esm', 'intake-esm Documentation', [author], 1)]

texinfo_documents = [
    (
        'index',
        'intake-esm',
        'intake-esm Documentation',
        author,
        'intake-esm',
        'One line description of project.',
        'Miscellaneous',
    )
]

ipython_warning_is_error = False
ipython_execlines = [
    'import intake',
    'import intake_esm',
    'import xarray',
    'import pandas as pd',
    'pd.options.display.encoding="utf8"',
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'intake': ('https://intake.readthedocs.io/en/stable/', None),
}


def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(src, app.config.html_context)
    source[0] = rendered


def setup(app):
    app.connect('source-read', rstjinja)


with open('catalogs.yaml') as f:
    catalogs = yaml.safe_load(f)


html_context = {'catalogs': catalogs['catalogs']}
