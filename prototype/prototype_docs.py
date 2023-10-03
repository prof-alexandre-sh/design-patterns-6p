'''
Script para gerar relatórios de alunos no Portal

Usamos um protótipo para gerar documentos de algum tipo. Clonamos o objeto protótipo
para a criação de outros tipos de relatórios
'''

import copy
import time

# Protótipo base para documentos
class DocumentPrototype:
    def clone(self):
        '''
        deepcopy: Faz uma cópia do objeto instanciado e, se esse objeto for composto (possuir outros objetos),
        faz a cópia deles também.

        copy: Faz uma cópia do objeto instanciado e cria referências dos objetos que compõe o mesmo.
        '''
        return copy.deepcopy(self)

    def render(self):
        pass

# Protótipo de documento HTML
class HTMLDocument(DocumentPrototype):
    # Simulando inicialização do documento
    def __init__(self):
        print("Inicializando um HTML...")
        print("Inicializando metadados...")
        print("Verificando servidor para obtenção dos dados...")
        print('\n')
        time.sleep(3)

    def render(self, name='', tipo='', aluno=''):
        return f"DOCUMENTO {name}\n<html>\n<body><p>Relatório de {tipo} do aluno {aluno}</p></body>\n</html>\n"

# Protótipo de documento PDF
class PDFDocument(DocumentPrototype):
    def __init__(self):
        print("Inicializando um PDF")

    def render(self):
        return "Conteúdo PDF"

# Gerenciador de protótipos
class PrototypeManager:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def create(self, name):
        if name in self._prototypes:
            return self._prototypes[name].clone()
        else:
            raise ValueError(f"Protótipo '{name}' não registrado.")

class Client:

    def gera_htmls(self):

        manager = PrototypeManager()

        manager.register("HTML", HTMLDocument())

        # OS 3 objetos abaixi, são clones do protótipo registrado
        html1 = manager.create("HTML")
        html2 = manager.create("HTML")
        html3 = manager.create("HTML")

        print(f"Protótipo criados: {len(manager._prototypes)}")
        print ("\n------\n")

        # Renderizamos 3 htmls copiando de 1 protótipo. Apenas 1 criação
        # Poderíamos usar subclasses para isso. Mas com os clones conseguimos fazer apenas uma criação
        # e obter 3 objetos com saídas diferentes
        print(html1.render('Relatório aluno 1', 'Notas', 'aluno 1'))
        print(html2.render('Relatório aluno 2', 'Faltas', 'aluno 2'))
        print(html3.render('Relatório aluno 3', 'Atividades', 'aluno 3'))

    def gera_htmls_sem_prot(self):

        html1 = HTMLDocument()
        print(html1.render('Relatório aluno 1', 'Notas', 'aluno 1'))
        html2 = HTMLDocument()
        print(html2.render('Relatório aluno 2', 'Faltas', 'aluno 2'))
        html3 = HTMLDocument()
        print(html3.render('Relatório aluno 3', 'Atividades', 'aluno 3'))

if __name__ == "__main__":
     cl = Client()
     cl.gera_htmls() # Com prototype. Criamos um objeto o clonamos os restantes
     #cl.gera_htmls_sem_prot()