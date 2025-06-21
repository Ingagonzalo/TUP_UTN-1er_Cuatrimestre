#!/bin/bash

read -p "Ingresá el nombre del archivo: " archivo

if [ -f "$archivo" ]; then
    echo "El archivo existe."
else
    echo "El archivo no existe."
fi

