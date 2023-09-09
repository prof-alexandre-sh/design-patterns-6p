from abc import ABC, abstractmethod # Classe built-in python para definir outras classes ou métodos abstratos

# Componente base
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent):
        pass

# Classe Folha: representa um arquivo
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent):
        print(f"{indent}Arquivo: {self.name}")

# Classe Composta: representa uma pasta
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = [] # Aqui vamos popular com objetos tipo FileSystemComponent.

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent):
        print(f"{indent}Pasta: {self.name}")
        for child in self.children:
            child.display(indent + "  ")

# Criar uma estrutura de arquivos
root = Folder("Raiz")
folder1 = Folder("Documentos")
folder2 = Folder("Fotos")
file1 = File("documento.txt")
file2 = File("foto1.jpg")
file3 = File("foto2.jpg")

root.add(folder1)
root.add(folder2)
folder1.add(file1)
folder2.add(file2)
folder2.add(file3)

# Exibir a estrutura de arquivos
# Veja que ao chamar o display da pasta root, tantos os objetos compostos quanto os simples 
# são tratados da mesma maneira
root.display(indent=" ")
#file1.display(indent=" ")