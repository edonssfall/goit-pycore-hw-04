# goit-pycore-hw-04

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

All commands run from the repo root.

Tasks 1–2 (`total_salary`, `get_cats_info`):

```bash
python main.py
```

Task 3 (directory tree):

```bash
python -m hws.hw03 /path/to/directory
```

Task 4 (assistant bot):

```bash
python -m hws.hw04
```

`-m` runs a script as a module, so imports of `share.py` from the repo root work without `PYTHONPATH`.

Bot commands: `hello`, `add <name> <phone>`, `change <name> <phone>`, `phone <name>`, `all`, `exit` / `close`.
