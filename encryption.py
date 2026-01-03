import os
import time
import sys

# key = 5

# Получить абсолютный путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Создать полный путь к файлу
file_sourse = os.path.join(script_dir, '1.txt')

# Использовать файл
with open(file_sourse, 'r') as file:
    content = file.read()
# print(content)
for key in range(1000):
    enc_content = ''.join([chr(ord(char) + key) for char in content])
    output = f"\r\rkey: {key}, {enc_content}"
    sys.stdout.write(output.ljust(len(content)*2))
    sys.stdout.flush()
    time.sleep(1.0)
    enc_file = os.path.join(script_dir, '2.txt')
    with open(enc_file, 'a') as file:
        file.write(f"key: {key}\n")
        file.write(enc_content + '\n\n')

'''dec_content = ''.join([chr(ord(char) - key) for char in enc_content])
print(dec_content)

dec_file = os.path.join(script_dir, '3.txt')
with open(dec_file, 'w') as file:
    file.write(dec_content)'''