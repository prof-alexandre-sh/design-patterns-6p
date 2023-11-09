class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado")

    def desligar(self):
        print(f"Motor {self.tipo} desligado")


class MotorFactory:
    def criar_motor(self, tipo):
        return Motor(tipo)


class Carro:
    def __init__(self, motor):
        self.motor = motor

    def ligar(self):
        print("Ligando o carro...")
        self.motor.ligar()

    def desligar(self):
        print("Desligando o carro...")
        self.motor.desligar()


# Exemplo de uso do Factory Method e Injeção de Dependência
motor_factory = MotorFactory()

motor_gasolina = motor_factory.criar_motor("Gasolina")
carro_gasolina = Carro(motor_gasolina)

motor_diesel = motor_factory.criar_motor("Diesel")
carro_diesel = Carro(motor_diesel)

# Testando os carros
carro_gasolina.ligar()
carro_gasolina.desligar()

carro_diesel.ligar()
carro_diesel.desligar()
