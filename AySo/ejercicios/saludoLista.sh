#!/bin/bash

# Verificamos si el archivo existe
if [ ! -f nombres.txt ]; then
    echo "El archivo 'nombres.txt' no existe."
    exit 1
fi

while read -r nombre; do
    echo "¡Hola, $nombre!"
done < nombres.txt
