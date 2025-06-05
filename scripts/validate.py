#!/usr/bin/env python3
"""
Validate `businesses.json` against its JSON Schema.

If validation fails, the script exits with a non-zero status code so
the GitHub Action will mark the pull request as failed.
"""

import json
import pathlib
import sys
from jsonschema import validate, ValidationError

ROOT = pathlib.Path(__file__).resolve().parents[1]
data_file   = ROOT / "data"   / "businesses.json"
schema_file = ROOT / "schema" / "businesses.schema.json"

try:
    with data_file.open() as f:
        data = json.load(f)
    with schema_file.open() as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)
    print("✅ businesses.json: validation passed")

except (json.JSONDecodeError, ValidationError) as err:
    print(f"❌ Validation error:\n{err}", file=sys.stderr)
    sys.exit(1)
