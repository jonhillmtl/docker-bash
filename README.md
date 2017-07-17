# docker_bash

Executes `bash` or `psql` on running Docker processes.

## Installation

`pip install git+https://github.com/jonhillmtl/docker-bash`

## Usage

`docker-bash`, which will log you into a bash shell on the running Docker web process.

or 

`docker-psql` which will log you into a psql shell on the running Docker postgres process.

## Options

```
Usage: docker-bash [options]

Options:
  -h, --help  show this help message and exit
  -v          verbose output
```

```
Usage: docker-psql [options]

Options:
  -h, --help  show this help message and exit
  -v          verbose output

```

## Todo

- add other commands and entry points
