from abc import ABC, abstractmethod

# Interface para a classe RealSubject
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Classe RealSubject
class RealImage(Image):
    def __init__(self, filename, file_size):
        self.filename = filename
        self.file_size = file_size
        self.load_image() # Faz o carregamento da imagem na sua criação

    def load_image(self):
        print(f"Carregando imagem: {self.filename}")

    def display(self):
        print(f"Exibindo imagem: {self.filename} de tamanho {self.file_size}")

# Proxy
class ImageProxy(Image):
    def __init__(self, filename, file_size):
        self.filename = filename # Referencia a imagem
        self.file_size = file_size
        self.real_image = None # Inicia como vazio. Inicialmente tem apenas a referencia a imagem

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename, self.file_size)
        self.real_image.display()

# Cliente
if __name__ == "__main__":


    print("COM PROXY")

    proxy1 = ImageProxy("imagem1.jpg", "500x500") # Não carrega a imagem na criação do proxy. Apenas quando precisamos (display)
    proxy2 = ImageProxy("imagem2.jpg", "600x600")

    print(proxy1.file_size) # Temos acesso as propriedades do objeto antes da sua instanciação

    #proxy1.display() # É carregada apenas quando chamado o display
    #proxy2.display()
    #proxy2.display() # Na segunda chamada ele apenas exibe. Cache

    print('\n')

    print ("SEM PROXY")

    sp1 = RealImage("imagem1.jpg", "500x500") # Carrega a imagem na criação. Mesmo não precisando de chamar o display no momento
    sp2 = RealImage("imagem2.jpg", "600x600")

    #sp1.display()
    #sp2.display()
    #sp2.display()