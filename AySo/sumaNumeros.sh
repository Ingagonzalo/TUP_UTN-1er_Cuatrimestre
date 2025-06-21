#!/bin/bash

suma=0
i=1

while [ $i -le 100 ]
do
  suma=$((suma + i))
  i=$((i + 1))
done

echo "La suma es: $suma"

