#!/bin/bash
# You need a wrapper script to use environment variables for now

CURDIR="$(dirname "$0")"

python3 "$CURDIR/../facenapalmscripts/validstats.py" "$TOOL_DATA_DIR/data/validation.tsv"
