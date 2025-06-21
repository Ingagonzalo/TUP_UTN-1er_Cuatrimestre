#!/bin/bash

read -p "Ingresá tu nota (0 a 10): " nota

if [ "$nota" -ge 0 ] && [ "$nota" -le 10 ]; then
    if [ "$nota" -lt 6 ]; then
        echo "Reprobado"
    elif [ "$nota" -ge 6 ] && [ "$nota" -le 8 ]; then
        echo "Aprobado"
    else
        echo "Excelente"
    fi
else
    echo "Nota inválida. Debe estar entre 0 y 10."
fi

