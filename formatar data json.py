import json

def formatar_datas_brasileiro(json_file):
    # Abre o arquivo JSON e carrega os dados
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Função para formatar a data
    def formatar_data(data_str):
        # Formato atual: "YYYY-MM-DD"
        # Converter para: "DD-MM-YYYY"
        partes = data_str.split('-')
        if len(partes) == 3:
            return f"{partes[2]}-{partes[1]}-{partes[0]}"
        else:
            return data_str  # Se não for uma data válida, retorna como está

    # Percorre cada objeto no arquivo JSON
    for obj in data:
        if 'data' in obj and isinstance(obj['data'], str):
            obj['data'] = formatar_data(obj['data'])

    # Salva de volta o arquivo JSON com as datas formatadas
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Exemplo de uso
if __name__ == "__main__":
    json_file = '\CursoPY\dados.json'  # Substitua pelo caminho do seu arquivo JSON
    formatar_datas_brasileiro(json_file)
    print(f"As datas no arquivo '{json_file}' foram formatadas para o formato brasileiro d-m-Y.")
