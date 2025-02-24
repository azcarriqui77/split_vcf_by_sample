#!/bin/bash

# Verifica que se proporciona un archivo como argumento
if [ $# -ne 1 ]; then
  echo "Uso: $0 <archivo.vcf>"
  exit 1
fi

file="$1"

# Verifica que el archivo existe
if [ ! -f "$file" ]; then
  echo "Error: El archivo '$file' no existe."
  exit 1
fi

while IFS=$'\n' read -r sample; do
  bcftools view -Oz -s "$sample" -o "${file/.vcf/.$sample.vcf}" "$file"
done < <(bcftools query -l "$file")