"""
This file contains common building, testing and deploying scripts. By
configuring pyproject.toml/[tool.poetry.scripts], scripts on this file can
be accessed directly by poetry, e.g.: $poetry run test
"""
import subprocess


def test():
    """
    Run all unittests. Equivalent to:
    `$poetry run python -u -m unittest discover`
    """
    subprocess.run(
        ['python', '-u', '-m', 'unittest', 'discover']
    )
