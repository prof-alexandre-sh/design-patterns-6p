class Handler:
    def __init__(self, successor=None):
        self.successor = successor # Cada handler pode receber seu sucessor como parâmetro

    def handle_request(self, sol_type):
        if self.successor:
            self.successor.handle_request(sol_type)

class Analista(Handler):
    def handle_request(self, sol_type):
        if sol_type == "Liberação/Revogação de acesso a aplicação":
            print(f"Analista aprova para '{sol_type}' ")
        else:
            print(f"Chamado do tipo '{sol_type} não por ser aprovado pelo Analista'")
            print()
            super().handle_request(sol_type)

class Gerente(Handler):
    def handle_request(self, sol_type):
        if sol_type == "Atribuir permissão elevada":
            print(f"Gerente aprova '{sol_type}'.")
        # Aqui implementamos um tipo de chamado onde precisamos
        # de dois aprovadores, o gerente e o diretor
        elif sol_type == "Banco de produção":
            print(f"Gerente aprova '{sol_type}'. Enviando aprovação para Diretor")
            print()
            super().handle_request(sol_type)
        # Aqui negamos o chamado e finalizamos (simplesmente não passamos adiante)
        elif sol_type=="Informações de clientes":
            print("Acesso negado e chamado finalizado")
        else:
            print(f"Chamado do tipo '{sol_type} não por ser aprovado pelo Gerente'")
            print()
            super().handle_request(sol_type)

class Diretor(Handler):
    def handle_request(self, sol_type):
        print("Diretor aprova todos tipos de chamados.")
        print(f"Aprovando {sol_type}")

def main():
    diretor = Diretor()
    gerente = Gerente(diretor)
    analista = Analista(gerente) # Analista é o premeiro nível

    sol_types = ["Liberação/Revogação de acesso a aplicação", "Atribuir permissão elevada", "Acesso a sistema financeiro", "Banco de produção", "Informações de clientes"]

    #analista.handle_request(sol_types[0]) # Aprova
    #analista.handle_request(sol_types[1]) # Passa para gerente
    #analista.handle_request(sol_types[2]) # Passa por todos até chegar no diretor]
    analista.handle_request(sol_types[4])



if __name__ == "__main__":
    main()
