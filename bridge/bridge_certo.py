'''
Ao invés de criar inúmeras classes, vamos criar abstrações para cada dimensão (implementação de alto nível).
Cada implementação vai conter uma herança de sua abstração e o relacionamento vai existir apenas
entre as abstrações e não as implementações.

No nosso cenário vamos ter uma relação de composição entre conteúdo e dispositivo (conteúdo depende do dispositivo).
O conteúdo irá conter um atributo que será do tipo do dispositivo. Assim, dentro de cada conteúdo conseguimos
interagir com os métodos dos dispositivos.

Aqui nosso código está desacoplado. Cada dimensão pode crescer separadamente. Se necessário, basta criar uma classe
extra e isso não irá comprometer seu código.

Podemos ainda adicionar mais dimensões, e essas ficarão desacopladas.
'''

class Dispositivo:
    def toca_conteudo(self, conteudo_tocar):
        pass

class Smartphone(Dispositivo):
    def toca_conteudo(self, conteudo_tocar):
        print(f"No smartphone, tocando {conteudo_tocar}")

class Playstation(Dispositivo):
    def toca_conteudo(self, conteudo_tocar):
        print(f"No Playstation, tocando {conteudo_tocar}")

class Conteudo:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo #Atributo dispositivo. Aqui vamos poder usar os métodos dos dispositivos

    def play(self):
        pass

class Podcast(Conteudo):
    def play(self):
        self.dispositivo.toca_conteudo("Podcast")

class Musica(Conteudo):
    def play(self):
        self.dispositivo.toca_conteudo("Musica")

sp = Smartphone()
musica = Musica(sp)
musica.play()

ps = Playstation()
pod = Podcast(ps)
pod.play()
