import os
import shutil

# Diretório onde estão os arquivos XML
diretorio_origem = "C:/Users/itarg/Downloads/tomeacu"

# Pasta de destino para as pastas com base no nome dos XMLs
pasta_destino = "C:/Users/itarg/Downloads/xmlSeparado"

# Verificar se a pasta de destino existe, se não, criá-la
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Listar todos os arquivos no diretório
arquivos = os.listdir(diretorio_origem)

# Dicionário para rastrear os arquivos com base no nome final (S-5003.xml)
arquivos_por_nome_final = {}

# Iterar sobre os arquivos e organizar em um dicionário
for arquivo in arquivos:
    if arquivo.endswith(".xml"):
        # Extrair o nome do arquivo final (S-5003.xml)
        nome_final = arquivo.split(".")[-2]

        if nome_final not in arquivos_por_nome_final:
            arquivos_por_nome_final[nome_final] = []

        arquivos_por_nome_final[nome_final].append(arquivo)

# Mover os arquivos para a pasta com base no nome final
for nome_final, arquivos in arquivos_por_nome_final.items():
    caminho_destino = os.path.join(pasta_destino, nome_final)
    
    # Verificar se a pasta de destino já existe, se não, criá-la
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
    
    for arquivo in arquivos:
        shutil.move(os.path.join(diretorio_origem, arquivo), os.path.join(caminho_destino, arquivo))

print("Arquivos movidos com sucesso!")
