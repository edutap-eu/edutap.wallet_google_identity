"""Sphinx configuration for edutap.wallet_google_identity."""

project = "edutap.wallet_google_identity"
author = "eduTAP"
copyright = "2026, LMU München and the eduTAP contributors"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

html_theme = "furo"
html_title = "edutap.wallet_google_identity"

exclude_patterns = ["_build"]

# Google's identity documentation blocks automated requests; checking those
# links reports failures that a browser does not see.
linkcheck_ignore = [
    r"https://developers\.google\.com/wallet/.*",
]
