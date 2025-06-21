#!/bin/bash

read -p "Ingresá una cadena: " texto

primeros8="${texto:0:8}"

echo "Los primeros 8 caracteres son: $primeros8"
