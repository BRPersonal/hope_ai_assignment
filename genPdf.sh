#!/bin/sh

if [ "$#" -ne 2 ]; then
  echo "Error: This script requires exactly two arguments."
  echo "Usage: $0 md-file-name pdf-file-name"
  exit 1
fi

pandoc $1 -o $2 --pdf-engine=pdflatex -H header.tex -V geometry:margin=1in

