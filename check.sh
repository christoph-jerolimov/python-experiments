#!/bin/bash

set -e

for file in *; do
    if [ -d "$file" ]; then
        echo $file
        cd $file
        echo "run ruff format --check"
        python -m ruff format --check
        echo "run ruff check"
        python -m ruff check
        echo "run mypy ."
        python -m mypy .
        cd ..
        echo
    fi
done
