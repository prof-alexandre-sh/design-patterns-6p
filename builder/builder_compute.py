# Classe que representa uma VM
class Computer:
    def __init__(self, name, cpu, ram, storage, os):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.os = os

    def display(self):
        print(f"Provisionando compute {self.name}...")
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("Armazenamento:", self.storage)
        print("Sistema Operacional:", self.os)

# Classe abstrata que define a interface para o Builder
class ComputerBuilder:
    def set_name(self):
        pass

    def set_cpu(self):
        pass

    def set_ram(self):
        pass

    def set_storage(self):
        pass

    def set_os(self):
        pass

    def get_computer(self):
        pass

# Implementação concreta do Builder para criar uma máquina "Developer"
class DevComputerBuilder(ComputerBuilder):
    def set_name(self, name):
        self.computer.name = name + '-DEV'

    def set_cpu(self, cpu):
        self.computer.cpu = "Intel Core i9"

    def set_ram(self, ram):
        self.computer.ram = "32GB DDR4"

    def set_storage(self, storage):
        self.computer.storage = "1TB SSD"

    def set_os(self):
        self.computer.os = 'Ubunutu - latest'

    def get_computer(self):
        return self.computer

# Implementação concreta do Builder para criar uma máquina "Cientista de Dados"
class DataComputerBuilder(ComputerBuilder):
    def set_name(self, name):
        self.computer.name = name + '-DATA'

    def set_cpu(self):
        self.computer.cpu = "AMD Ryzen 9"

    def set_ram(self, ram):
        self.computer.ram = ram

    def set_storage(self, storage):
        self.computer.storage = storage

    def set_os(self, os):
        self.computer.os = os

    def get_computer(self):
        return self.computer

# Diretor que cria o computador usando o Builder
# NÃO É OBRIGATÓRIO
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    # Diretor pode usar o builder da maneira que desejar
    # Aqui separamos a construção da representação do objeto
    def create_computer(self):
        self.builder.computer = Computer(None, None, None, None) # Inicializamos sem valores. O Builder fará isso
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_os()
        return self.builder.get_computer()


# Cliente
def main():

    '''
    Sem diretor
    '''

    # A construição do objeto fica aqui
    # Enquanto sua definição está na classe
    builder_dev = DevComputerBuilder()
    builder_dev.computer = Computer(None, None, None, None, None)
    builder_dev.set_name("alexandre-ubuntu")
    #print("DISPLAY DEV VM")
    #builder_dev.get_computer().display()

    print("--------")

    builder_data = DataComputerBuilder()
    builder_data.computer = Computer(None, None, None, None, None)
    builder_data.set_name("alexandre-ml")
    builder_data.set_cpu()
    builder_data.set_ram("32GB DDR4")
    builder_data.set_storage("500GB SSD NVMe")
    builder_data.set_os("Windows 11")
    builder_data.get_computer().display()


    '''
    Usando diretor. Código comentado para testes

    # Crie um diretor para criar um computador "Gamer"
    gamer_builder = GamerComputerBuilder()
    gamer_director = ComputerDirector(gamer_builder)
    gamer_computer = gamer_director.create_computer()

    # Exiba as especificações do computador "Gamer"
    print("Computador Gamer:")
    gamer_computer.display()

    print("\n")

    # Crie um diretor para criar um computador "Desenvolvedor"
    developer_builder = DeveloperComputerBuilder()
    developer_director = ComputerDirector(developer_builder)
    developer_computer = developer_director.create_computer()

    # Exiba as especificações do computador "Desenvolvedor"
    print("Computador de Desenvolvedor:")
    developer_computer.display()

    '''

if __name__ == "__main__":
    main()