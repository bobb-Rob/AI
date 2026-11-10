# first-test-project

A small Python project for learning AI engineering. It includes a "hello LLM" script that sends a single prompt to OpenAI and prints the reply.

## Requirements

- Python 3.15 or newer
- [uv](https://docs.astral.sh/uv/) (the package and project manager)
- An OpenAI API key with credits on the account

## Installation

1. **Install uv** if you don't have it yet:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository** and move into it:

   ```bash
   git clone <repo-url>
   cd first-test-project
   ```

3. **Install dependencies.** This creates a `.venv` folder and installs everything in `uv.lock`, including the dev tools:

   ```bash
   uv sync
   ```

   uv downloads Python 3.15 automatically if it isn't already installed.

4. **Add your API key.** Create a file named `.env` in the project root:

   ```bash
   OPENAI_API_KEY=sk-...
   ```

   `.env` is listed in `.gitignore`, so your key won't be committed.

## Running the project

Send one prompt to the LLM and print the reply:

```bash
uv run python hello_llm.py
```

To change the prompt or the model, edit `input` and `model` in [hello_llm.py](hello_llm.py).

Run the package entry point:

```bash
uv run first-test-project
```

## Development

Run the tests:

```bash
uv run pytest -v
```

Lint and format the code:

```bash
uv run ruff check .         # report problems
uv run ruff check . --fix   # fix what can be fixed automatically
uv run ruff format .        # format the code
```

## Project structure

```
first-test-project/
├── hello_llm.py                 # sends one prompt to OpenAI and prints the reply
├── src/first_test_project/      # package source code
├── tests/                       # pytest tests
├── pyproject.toml               # project metadata and dependencies
├── uv.lock                      # pinned dependency versions
└── .env                         # your API key (not committed)
```

## Troubleshooting

| Error | Fix |
|---|---|
| `openai.AuthenticationError` (401) | Check that `OPENAI_API_KEY` in `.env` is correct. |
| `openai.RateLimitError` (429): "no credits remaining" | Add credits at https://platform.openai.com/settings/organization/billing/. |
| `ModuleNotFoundError: first_test_project` | Run `uv sync` so the package gets installed into `.venv`. |
