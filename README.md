![main_build_status](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

# EDU project

## Project

This is _Cracking the Caesar Cypher_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.11
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

Small program that can interpret texts encrypted by the Caesar cipher.

#### Install steps adapted for Poetry

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
