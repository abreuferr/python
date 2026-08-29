#!/usr/bin/env python3
"""Validação mínima dos exemplos, sem executar programas gráficos ou interativos."""

import ast
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_DIRECTORIES = {".git", ".venv", "venv", "__pycache__"}
PYTEST_TARGETS = (
    "usp_ime/src/bhaskara_test.py",
    "usp_ime/src/fatorial_pytest.py",
    "usp_ime/src/pyteste.py",
)


def python_files():
    for path in ROOT.rglob("*.py"):
        if not EXCLUDED_DIRECTORIES.intersection(path.parts):
            yield path


def validate_syntax():
    failures = []
    files = list(python_files())
    for path in files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, UnicodeDecodeError, SyntaxError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")
    if failures:
        print("Falhas de sintaxe:", *failures, sep="\n")
        return False
    print(f"Sintaxe: {len(files)} arquivos válidos")
    return True


def validate_tests():
    command = [sys.executable, "-m", "pytest", "-q", *PYTEST_TARGETS]
    result = subprocess.run(command, cwd=ROOT, check=False)
    return result.returncode == 0


if __name__ == "__main__":
    syntax_ok = validate_syntax()
    tests_ok = validate_tests() if syntax_ok else False
    raise SystemExit(0 if syntax_ok and tests_ok else 1)
