# Pydantic AI Starter

[![CI](https://github.com/cherninlab/pydantic-ai-starter/actions/workflows/CI.yml/badge.svg)](https://github.com/cherninlab/pydantic-ai-starter/actions/workflows/CI.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

This is a minimal starter project for [PydanticAI](https://ai.pydantic.dev), using [**uv**](https://docs.astral.sh/uv/getting-started/installation/) to manage installations and run commands.

[![Open in GitPod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/cherninlab/pydantic-ai-starter)

Need inspiration? Check out the official [Pydantic AI Examples](https://github.com/pydantic/pydantic-ai/tree/main/examples).

## Table of contents

1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Docker / Docker Compose](#docker--docker-compose)
5. [Development & CI](#development--ci)
6. [License](#license)

## Requirements

- [Python](https://www.python.org/) 3.9 or higher
- [**uv**](https://docs.astral.sh/uv/getting-started/installation/) installed

## Getting Started

Clone this repository and install dependencies:

```bash
git clone https://github.com/cherninlab/pydantic-ai-starter.git
cd pydantic-ai-starter
uv sync
```

> By default, `uv sync` reads pyproject.toml and installs the [project] dependencies.

## Usage

Run the main script:

```bash
uv run --env-file .env -- python -m pydantic_ai_starter
```

### API Providers

This starter installs multiple providers via `pydantic-ai-slim` extras:

- openai
- anthropic
- mistral
- groq
- logfire

Configure your keys (if needed)

## Docker / Docker Compose

1. Build with Docker:

```bash
docker-compose build
```

2. Run:

```bash
docker-compose up
```

> This will run `__main__.py` by default inside the container.

## Development & CI

- GitHub Actions in `.github/workflows/CI.yml` for linting (`pre-commit`)
- Pre-commit config in `.pre-commit-config.yaml`
- Example test in `tests/test_example.py`

## License

[MIT](https://choosealicense.com/licenses/mit/)

<p align="center"><b>Happy coding with PydanticAI! 🚀</b></p>
