import re
import sys

def clean_info_field(info):
    # Elimina espacios en blanco, punto y coma y signos igual del campo INFO
    info = re.sub(r'[;\s=]', '_', info)
    return info

def clean_vcf(input_vcf, output_vcf):
    with open(input_vcf, 'r') as infile, open(output_vcf, 'w') as outfile:
        for line in infile:
            if line.startswith('#'):
                outfile.write(line)
            else:
                fields = line.strip().split('\t')
                info_field = fields[7]
                fields[7] = clean_info_field(info_field)
                outfile.write('\t'.join(fields) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python clean_vcf.py <archivo_vcf_entrada> <archivo_vcf_salida>")
        sys.exit(1)

    input_vcf = sys.argv[1]
    output_vcf = sys.argv[2]
    clean_vcf(input_vcf, output_vcf)
    print(f'Archivo limpiado: {output_vcf}')
