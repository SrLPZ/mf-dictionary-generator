import sys
import os

def generate_keys(input_file):
    try:
        with open(input_file, 'rb') as bin_file:
            binary_data = bin_file.read()

        keys = [binary_data[i:i+6].hex().upper() for i in range(0, 32 * 6, 6)]
        unique_keys = list(set(keys))

        dir_name = os.path.dirname(input_file)
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(dir_name, f"{file_name}.dic")

        with open(output_file, 'w') as keys_file:
            keys_file.write('\n'.join(unique_keys))
        print(f"Dictionary has been generated and written to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
if len(sys.argv) < 2:
    print("Usage: python mf-bin2dic.py input_file.bin")
else:
    input_file_path = sys.argv[1]
    generate_keys(input_file_path)
