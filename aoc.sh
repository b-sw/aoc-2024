#!/bin/bash
if [ -z "$1" ]; then
  echo "Usage: $0 <day>"
  exit 1
fi

if ! [[ "$1" =~ ^[1-9]$|^1[0-9]$|^2[0-5]$ ]]; then
  echo "Error: Day must be a number between 1 and 25"
  exit 1
fi

DAY_DIR="day$1"
mkdir -p "$DAY_DIR"

touch "$DAY_DIR/solution.py"
touch "$DAY_DIR/input.txt"

open -a "Google Chrome" "https://adventofcode.com/2024/day/$1"

echo "Directory and files for day $1 created successfully."