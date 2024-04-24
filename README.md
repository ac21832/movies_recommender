# Instructions

1. Install poetry following the official [docs](https://python-poetry.org/docs/#installing-with-pipx).
2. Create a project with `poetry new <project-name>`.
3. Navigate to your project. Open a terminal in the directory, or use `cd <project-name>`.
4. Create virtual environment within your project with `poetry shell`.
5. Create an account on [PyPi][https://pypi.org]
6. Build the project `poetry build`
7. Configure your PyPi token in poetry with: `poetry config pypi-token.pypi <your-token>`
8. Publish your package with `poetry publish`
