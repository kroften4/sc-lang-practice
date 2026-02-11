#!/usr/bin/env bash

LANGS_PATH=$1
OUTPUT_PATH=$2

echo [`find $LANGS_PATH -type f -name "*" -printf "\"%f\", " | sed "s/, $//"`] > $OUTPUT_PATH
