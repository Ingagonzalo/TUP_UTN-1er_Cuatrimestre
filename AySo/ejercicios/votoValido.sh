#!/bin/bash

read -p "Ingresá tu nombre: " nombre
read -p "Ingresá tu edad: " edad

if [ "$edad" -ge 16 ]; then
    echo "$nombre, puede votar."
else
    echo "$nombre, todavia no puede votar."
fi

