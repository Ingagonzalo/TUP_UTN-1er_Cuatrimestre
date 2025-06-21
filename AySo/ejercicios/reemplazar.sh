#!/bin/bash

mensaje="Hubo un error en el sistema. Otro error ocurrió después."

# Reemplazo usando sustitución de Bash
nuevoMensaje=${mensaje//error/problemita}

echo "Original: $mensaje"
echo "Modificado: $nuevoMensaje"
