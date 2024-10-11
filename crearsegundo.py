import json
import requests

def get_country_from_ip(ip):
    try:
        # Llamada a la API para obtener información de la IP
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        
        # Verificar que la respuesta sea exitosa
        if response.status_code == 200:
            data = response.json()
            # Verifica si la clave 'country_name' está presente
            if 'country_name' in data:
                return data['country_name']
            else:
                return 'Unknown (No country found in response)'
        else:
            print(f'Error en la respuesta: {response.status_code} para IP {ip}')
            return 'Unknown (Invalid response status)'
    except requests.exceptions.RequestException as e:
        print(f'Error al realizar la solicitud para la IP {ip}: {e}')
        return 'Unknown (Request Exception)'
    except json.JSONDecodeError:
        print(f'Error al decodificar el JSON para la IP {ip}. Respuesta: {response.text}')
        return 'Unknown (JSON Decode Error)'

def create_second_json(input_file_path, output_file_path):
    try:
        # Leer el archivo 2k.json
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            data_2k = json.load(input_file)

        # Crear la nueva lista para el nuevo JSON
        second_data = []

        for entry in data_2k:
            ip = entry.get('ip')
            country = get_country_from_ip(ip)  # Obtener país desde la IP
            id_value = entry.get('id')  # Obtener id (asegúrate de que exista)
            
            # Crear un nuevo diccionario con la información deseada
            new_entry = {
                'id': id_value,
                'ip': ip,
                'country': country
            }
            second_data.append(new_entry)

        # Escribir el nuevo archivo JSON
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(second_data, output_file, indent=2)

        print(f'Archivo creado: {output_file_path}')
    except Exception as e:
        print(f'Error: {e}')

# Especifica las rutas de entrada y salida
input_file_path = 'securityWebAnalysis/2k.json'  # Nombre del archivo 2k.json
output_file_path = 'securityWebAnalysis/segundo.json'  # Nombre del nuevo archivo

# Llama a la función
create_second_json(input_file_path, output_file_path)
