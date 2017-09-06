import hashlib

a = input("Digite uma senha: ")
b = hashlib.sha512(a.encode()).hexdigest()
b = b.upper()
print(b)
