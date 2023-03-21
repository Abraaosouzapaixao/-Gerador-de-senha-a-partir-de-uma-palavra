import random
import string

def generate_password(word, length):
    # Adiciona um número aleatório entre 100 e 999 no final da palavra
    password = word + str(random.randint(100, 999))
    
    # Adiciona caracteres aleatórios na senha até que o comprimento desejado seja atingido
    while len(password) == length - 1:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    # Embaralha a senha
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

# Loop 
while True:
    print("Digite 'sair' a qualquer momento para sair.")
    word = input("Digite uma palavra para gerar uma senha: ")
    if word == "sair":
        break
    length = int(input("Digite o comprimento desejado da senha: "))
    password = generate_password(word, length)
    print("Sua senha é:", password)
