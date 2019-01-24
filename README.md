# b2sw

![build](https://img.shields.io/travis/com/CarlosDomingues/b2sw.svg?style=popout-square) ![coverage](https://img.shields.io/codecov/c/gh/CarlosDomingues/b2sw.svg?style=popout-square) ![license](https://img.shields.io/github/license/CarlosDomingues/b2sw.svg?style=popout-square)

## Introduction

**b2sw** is a simple app for fetching Star Wars planet information.

## API

## Deploy

## Architecture

![b2sw architecture](https://user-images.githubusercontent.com/11181378/51699710-9a235980-1ff4-11e9-9c7e-6a2021637ac0.png 'b2sw architecture')

## Development Enviroment

**b2sw** requires Pytho 3.6+ and [Poetry](https://github.com/sdispater/poetry) for dependency management. After meeting those requirements, go to the project root folder, then:

1. Install dependencies:

```bash
poetry install
```

2. Run unit tests:

```bash
poetry run test
```

3. (Optional for [Visual Studio Code](https://code.visualstudio.com/) users) Set up a workspace by creating a `b2sw.code-workspace` file with the following content:

```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "python.pythonPath": "<POETRY-VENV-PATH>/b2sw-py3.6/Scripts/python.exe"
  }
}
```

To find your actual poetry virtual enviroment path run:

```bash
poetry run which python
```

**Note to Windows users**: use **\\\\** instead of **/** to join paths.

## Licensing
