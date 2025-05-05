import random
boneco = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
          r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']


palavras = ["facil","medio"]

numeroaleatorio = random.randint(0, len(palavras)-1)
palavraSelecionada = palavras[numeroaleatorio]
letrasCertas = ['_'] * len(palavraSelecionada)
letrasErradas = []
tentativas = 7

while(tentativas != 0):
    while True:
        letraDigitada = input("Digite uma letra: ").lower()
        if len(letraDigitada) == 1 and letraDigitada.isalpha():
            break
        else:
            print("Por favor, digite apenas uma letra.")
    if letraDigitada in palavraSelecionada:
        for i in range(len(palavraSelecionada)):
            if palavraSelecionada[i] == letraDigitada:
             letrasCertas[i] = letraDigitada
        print(letrasCertas)
        if  "_" not in letrasCertas:
            print("Parabêns você ganhou")
            break
    else:
        if letraDigitada in letrasErradas:
            print ("essa letra ja foi digitada!!!")
            print (letrasErradas)
        else:
            tentativas = tentativas - 1
            letrasErradas.append(letraDigitada)
            print(boneco[tentativas])
            print(letrasErradas)
