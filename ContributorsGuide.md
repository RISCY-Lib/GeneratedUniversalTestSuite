# guts Contributor's Guide

## Development Environment
A devlopement environment has been created. To use install docker and docker compose.

Then:

```docker build -t guts_dev:1.0 .```

```docker compose up```

Then connect to the docker image through the VSCode Docker/Dev Container extension (or similar on other IDE).

## Verifying the Project

A ```tox``` environment has been setup to check the [coding styles](#Coding-Style) and the ```pytest``` tests.

## PyTest Tests
Testing for this project is done with ```pytest```.
These test's live in the ./tests directory.

## Coding Style
Coding style guidelines can be found [here](./CodingStyle.md)

Coding style requirements can be checked by running ```flake8 guts tests``` from
  the project top directory.

Additionally, the static-typing requirement of the CodingStyle can be checked
  by running ```mypy guts```
