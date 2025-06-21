#!/bin/bash

contrasenia=""

until [ "$contrasenia" = "secreto" ]
do
  read -p "Ingresa la contraseña: " contrasenia
done

echo "¡Contraseña aceptada!"

