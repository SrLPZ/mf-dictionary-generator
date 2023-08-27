import sys
import os

def generate_keys(input_file):
    try:
        with open(input_file, 'rb') as bin_file:
            binary_data = bin_file.read()
        
        # Dividir los datos en segmentos de 6 bytes y convertirlos a hexadecimales
        keys = [binary_data[i:i+6].hex().upper() for i in range(0, len(binary_data), 6)]
        
        # Calcular el punto de división para las dos mitades
        half_length = len(keys) // 2

        # Crear una lista de claves intercaladas
        interleaved_keys = []
        for i in range(half_length):
            interleaved_keys.append(keys[i])
            interleaved_keys.append(keys[i + half_length])
        
        # Crear una lista para mantener el orden original de las claves únicas
        unique_keys_in_order = []
        seen_keys = set()

        # Mantener el orden original y eliminar claves duplicadas
        for key in interleaved_keys:
            if key not in seen_keys:
                seen_keys.add(key)
                unique_keys_in_order.append(key)
        
        dir_name = os.path.dirname(input_file)
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(dir_name, f"{file_name}.dic")

        # Abrir el archivo de texto en modo escritura
        with open(output_file, 'w') as keys_file:
        # Escribir cada clave hexadecimal en el archivo de texto en el orden intercalado
            for index, key in enumerate(unique_keys_in_order, start=1):
                keys_file.write(f"{key}\n")

        print(f"Dictionary has been generated and written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Ejemplo de uso:
if len(sys.argv) < 2:
    print("Usage: python script_name.py input_file.bin")
else:
    input_file_path = sys.argv[1]
    generate_keys(input_file_path)
