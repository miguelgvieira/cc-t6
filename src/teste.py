import filecmp
import os

from main import main

input_dir = 'entrada/'

output_dir = 'saida_teste/'
compiled_dir = 'saida_compilada/'

arquivos_entrada = 'entrada_execucao/'
arquivos_saida = 'saida/'

arquivos_saida_teste = 'saida_execucao_teste'

input_files = os.listdir('entrada/')
input_files.sort()

diffs = []
iguais = []

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

for file in input_files:
    # to_look = ["20."]
    to_look = [f"{i}." for i in range(1, 25)]
    for v in to_look:
        if file.startswith(v):
            print(file)

            main([f"{input_dir}/{file}", f"{output_dir}/{file}.c"])

            if not os.path.isdir(compiled_dir):
                os.makedirs(compiled_dir)
            try:
                if len(to_look) > 0:
                    os.system(f"gcc {output_dir}/{file}.c -o {compiled_dir}/{file}.out")

                    entrada = read_file(f"{arquivos_entrada}/{file}")
                    saida = read_file(f"{arquivos_saida}/{file}")

                    os.system(f"printf '{entrada}' | {compiled_dir}/{file}.out > {arquivos_saida_teste}/{file}")

                    if filecmp.cmp(f"{arquivos_saida_teste}/{file}", f"{arquivos_saida}/{file}"):
                        iguais.append(file)
                        print("Arquivos iguais", file)
                    else:
                        diffs.append(file)
                        print("Arquivos diferentes: ", file)
            except Exception as e:
                diffs.append(file)

print("Arquivos iguais: ", iguais)
print("Arquivos diferentes: ", diffs)