# goit-pycore-hw-04

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Tasks 1–2 (`total_salary`, `get_cats_info`) run from `main.py` in the repo root:

```bash
python main.py
```

Task 3 (directory tree) and task 4 (assistant bot) run directly from `hws/`:

```bash
export PYTHONPATH=..
python hws/hw03.py
```

```bash
python hws/hw03.py
```

`hw03.py` imports `share.py` from the repo root, so it needs `PYTHONPATH=..`.

Bot commands: `hello`, `add <name> <phone>`, `change <name> <phone>`, `phone <name>`, `all`, `exit` / `close`.
