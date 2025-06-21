#!/bin/bash

read -p "Ingresá un texto: " texto

minusculas=$(echo "$texto" | tr '[:upper:]' '[:lower:]')

echo "Texto en minúsculas: $minusculas"
