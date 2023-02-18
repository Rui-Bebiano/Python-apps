import os
import math

#Pasta raíz --------------
root_dir = os.getcwd()

#Cabeçalho da tabela --------------
print("\n  "+53*"_"+"\n | Tema"+36*" "+"| Ficheiros |\n"+" |-"+40*"-"+"|"+11*"-"+"|")

#Inicialização do contador de pastas que contêm ficheiros --------------
i=0

#A função os.walk() percorre todo o sistema de pastas a partir da raíz  --------------
for dir_path, dir_names, file_names in os.walk(root_dir):
    
    # Ações a realizar caso seja uma pasta "To Process" contendo ficheiros --------------
    if ('To Process' in dir_names):
        to_process_dir = os.path.join(dir_path, 'To Process')
        tema = to_process_dir.rsplit("\\")[-2].replace("_"," ")
        num_files = len([f for f in os.listdir(to_process_dir) if os.path.isfile(os.path.join(to_process_dir, f))])
        # Escreve o tema e o nr de ficheiros, caso existam --------------
        if num_files>0:
            # Espaçamento entre elementos da tabela --------------
            spaces1 = (37-len(tema))*" "
            spaces2 = (4-math.floor(math.log10(num_files)))*" "
            spaces3 = 2*" "
            # Escreve o tema e o nr de ficheiros --------------
            print(" | ",tema,spaces1,"|",spaces2,num_files,spaces3,"|")
            i+=1

# Indicação de que não há ficheiros --------------
if i==0:
    print(" | Não há ficheiros! :)"+20*" "+"|"+6*" "+"-"+4*" "+"|")

# Final da tabela --------------
print(" |"+41*"_"+"|"+11*"_"+"|\n")