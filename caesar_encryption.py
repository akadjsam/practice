import ciphertext

text = input("암호화 할 문장을 입력하세요 : ")
num = 3
enc = ciphertext.Cipher()
print(enc.encryption(text, num))
print(enc.decryption())