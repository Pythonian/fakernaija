"""Sphinx doc configurations."""

import sys
from pathlib import Path

# Use Path to define the root directory
project_root = Path(__file__).resolve().parents[2]

# Insert the project root into the sys.path
sys.path.insert(0, str(project_root))


def get_version() -> str:
    """Function to extract the version from fakernaija/__init__.py."""
    version_file = (
        Path(__file__).resolve().parent.parent.parent / "fakernaija" / "__init__.py"
    )
    with version_file.open() as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[-1].strip().strip('"')
    msg = "Version not found in __init__.py"
    raise RuntimeError(msg)


project = "Fakernaija"
copyright = "2024, Seyi Pythonian"  # noqa: A001
author = "Seyi Pythonian"
version = get_version()
release = version

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "myst_parser",
    "notfound.extension",
]

templates_path = ["_templates"]
suppress_warnings = ["epub.unknown_project_files"]
exclude_patterns: list[str] = []
copybutton_exclude = ".linenos, .gp, .go"
copybutton_prompt_text = ">>> "
html_theme = "furo"
html_show_sphinx = False
html_title = f"Fakernaija v{get_version()}"
html_theme_options = {
    "source_repository": "https://github.com/Pythonian/fakernaija",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Pythonian/fakernaija",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
