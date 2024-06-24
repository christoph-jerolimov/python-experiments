#!/bin/bash

set -e

for file in *; do
    if [ -d "$file" ]; then
        echo $file
        cd $file
        echo "run ruff format"
        python -m ruff format
        cd ..
        echo
    fi
done
