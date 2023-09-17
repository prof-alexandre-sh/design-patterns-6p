class Formatacao:
    '''
    Objeto com caractrísticas compartilháveis
    '''
    def __init__(self, fonte, tamanho, caracter):
        self.fonte = fonte
        self.tamanho = tamanho
        self.caracter = caracter

    def mostrar(self, linha):
        print(f'Caracter {self.caracter} com a fonte {self.fonte} de tamanho {self.tamanho} na linha {linha}')

class Caracter:
    '''
    Objeto caracter, pode conter características compartilháveis
    e únicas
    '''
    def __init__(self, linha, formatacao):
        self.linha = linha # Característica única
        self.formatacao = formatacao # Característica compartilhada

    def mostrar(self):
        self.formatacao.mostrar(self.linha)

class FlyweightFabrica:
    '''
    Fábrica dos objetos com características compartilhadas.
    Gerencia a criação dos objetos
    '''
    _formatos = {}

    '''
    Esse é um método estático. Podemos chamar ele diretamente da classe sem instanciar um objeto.
    Isso vai permitir a ideia de "economia" do Flyweight
    '''
    @staticmethod
    def get_formatacao(fonte, tamanho, caracter):
        chave = (fonte, tamanho, caracter) # Usamos um tupla (imutável) pra representar uma árvore única
        if chave not in FlyweightFabrica._formatos:
            FlyweightFabrica._formatos[chave] = Formatacao(fonte, tamanho, caracter)
        return FlyweightFabrica._formatos[chave]

if __name__=='__main__':
    formatos = []

    # Criar formatações de caracteres - compartilhados
    formatacao_1 = FlyweightFabrica.get_formatacao("calibri", "12", "a")
    formatacao_2 = FlyweightFabrica.get_formatacao("arial", "11", "b")

    # Criar caracteres individuais
    formatos.append(Caracter("linha 1", formatacao_1))
    formatos.append(Caracter("linha 2", formatacao_1)) # Aqui ele não cria um objeto novo. Reutiliza o que já existe
    formatos.append(Caracter("linha 2", formatacao_2))
    formatos.append(Caracter("linha 3", formatacao_2))

    for caracter in formatos:
        caracter.mostrar()

    # Mostrando os objetos criados - Perceba que não são instancias novas
    print(len(FlyweightFabrica._formatos))