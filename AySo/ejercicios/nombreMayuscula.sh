#!/bin/bash

read -p "Ingresá tu nombre: " nombre
read -p "Ingresá tu apellido: " apellido


nombreMayus=$(echo "$nombre" | tr '[:lower:]' '[:upper:]')
apellidoMayus=$(echo "$apellido" | tr '[:lower:]' '[:upper:]')

echo "Nombre completo en mayúsculas: $nombreMayus $apellidoMayus"
