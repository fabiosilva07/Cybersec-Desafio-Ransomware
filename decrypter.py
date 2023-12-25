import os
import pyaes

## O arquivo criptografado
file_name = "teste.txt.encrypted"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Excluir o arquivo encriptado
os.remove(file_name)

## Informando chave para decriptar
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Descriptografando o arquivo
decrypted_data = aes.decrypt(file_data)

## Criar arquivo decriptado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypted_data)
new_file.close()
