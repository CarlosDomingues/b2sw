# b2sw

![build](https://img.shields.io/travis/com/CarlosDomingues/b2sw.svg?style=popout-square) ![maintainability](https://img.shields.io/codeclimate/maintainability/CarlosDomingues/b2sw.svg?style=popout-square) ![issues](https://img.shields.io/codeclimate/issues/CarlosDomingues/b2sw.svg?style=popout-square) ![coverage](https://img.shields.io/codecov/c/gh/CarlosDomingues/b2sw.svg?style=popout-square) ![license](https://img.shields.io/github/license/CarlosDomingues/b2sw.svg?style=popout-square)

## Introduction

**b2sw** is a simple app for fetching Star Wars planet information. It's meant to be an example of a simple microservice that runs on Amazon's Elastic Containter Service.

## Architecture

![b2sw architecture](https://user-images.githubusercontent.com/11181378/51699710-9a235980-1ff4-11e9-9c7e-6a2021637ac0.png 'b2sw architecture')

**b2sw** has three interfaces with external services:

- [Amazon's DynamoDB](https://aws.amazon.com/pt/dynamodb/): The app's main and only database, used to store and retrieve planet information. See **datamodel.py** for the interface implementation.
- [Amazon's API Gateway](https://aws.amazon.com/api-gateway/): Acts as a 'front door' to our application, providing security, monitoring and load balancing. See **app.py** for the interface implementation.
- [The Star Wars API](https://swapi.co/): A RESTful webservice for Star Wars information retrieval. Used to complement the information stored by our app. See **swapiutils.py** for the interface implementation.

## API

## Deploy

## Development Enviroment

**b2sw** requires Pytho 3.6+ and [Poetry](https://github.com/sdispater/poetry) for dependency management. After meeting those requirements, go to the project root folder, then:

1 - Install dependencies:

```bash
poetry install
```

2 - Run unit tests:

```bash
poetry run test
```

3 - (Optional for [Visual Studio Code](https://code.visualstudio.com/) users) Set up a workspace by creating a `b2sw.code-workspace` file with the following content:

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
