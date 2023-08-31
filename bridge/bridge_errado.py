'''
Abaixo vemos um exemplo onde, para cada dimensão que eu desejo adicionar (Conteúdo, Dispositivo, Tipo de conta)
a complexidade e o tamanho do código aumenta devido a quantidade de classes
'''


# Tipo de conteúdo
class Podcast:
    def play(self):
        print("Toca podcast")

class Musica:
    def play(self):
        print("Toca musica")

# Dispositivo para cada conteúdo
class SmartphonePodcast:
    def play(self):
        print("Ouvindo podcast pelo smartphone")
    
class PlaystationPodcast:
    def play(self):
        print("Ouvindo podcast pelo playstation")

class SmartphoneMusica:
    ddef play(self):
        print("Ouvindo música pelo smartphone")

class PlaystationMusica:
    ddef play(self):
        print("Ouvindo música pelo playstation")

# Tipo de conta (Premium, basic)...
