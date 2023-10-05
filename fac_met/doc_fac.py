from abc import ABC, abstractmethod

# Interface para documentos
class Document(ABC):
    @abstractmethod
    def create(self):
        pass

# Implementação de documentos
class TextDocument(Document):
    def create(self):
        return "Criando um documento de texto"

class PDFDocument(Document):
    def create(self):
        return "Criando um documento PDF"

# Fábrica abstrata para criar documentos com base em uma string
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, document_type):
        pass

# Implementação de fábricas de documentos com base em uma string
class StringBasedDocumentFactory(DocumentFactory):
    '''
    A fábrica implementa a lógica de criação e o client não tem acesso a essa complexidade (desacoplamento).
    Estamos encapsulando o comportamente de INSTANCIAÇÃO. Desacoplamento máximo
    '''
    def create_document(self, document_type):
        if document_type.lower() == "text":
            return TextDocument()
        elif document_type.lower() == "pdf":
            return PDFDocument()
        else:
            raise ValueError("Tipo de documento não suportado")

# Função para criar e usar documentos
def create_and_use_document(factory, document_type): #  Fexibilidade para criarmos os objetos no client
    document = factory.create_document(document_type)
    print(document.create())

# Exemplo de uso da fábrica com base em uma string
if __name__ == "__main__":
    print("Exemplo usando a fábrica")
    
    string_factory = StringBasedDocumentFactory()
    
    create_and_use_document(string_factory, "text")
    create_and_use_document(string_factory, "pdf")
