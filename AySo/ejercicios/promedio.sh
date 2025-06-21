#!/bin/bash

suma=0

for i in {1..5}; do
    read -p "Ingresá el número $i: " num
    suma=$((suma + num))
done

promedio=$((suma / 5))

echo "El promedio es: $promedio"


