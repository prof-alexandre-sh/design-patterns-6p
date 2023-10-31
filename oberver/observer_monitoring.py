from abc import ABC, abstractmethod
import random

# Classe abstrata que define o Observador
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Classe concreta que implementa o Observador
class GrupoEmailAdmins(Observer):

    def update(self, sujeito):
        if sujeito.memory_usage >= sujeito.threshold: 
            print(f"Enviando e-mail para Admins: OOMKILL!") # Notifica todos e mata processo
            sujeito.running = False

# Classe concreta que implementa o Observador
class GrupoEmailUsers(Observer):

    def update(self, sujeito):
        if sujeito.memory_usage >= 70: 
            print(f"Enviando email para usuários: Memória com alto uso!") # Apenas notifica grupo de usuários

# Classe que atua como o Sujeito (monitor de memória)
class MemorySubject:
    def __init__(self, threshold):
        self.observers = []
        self.memory_usage = 0  # Simulando a utilização de memória
        self.threshold = threshold  # Limite de memória antes da notificação
        self.running = True

    def add_observer(self, observer): # Assinatura
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def simulate_memory_usage(self):
        self.memory_usage = random.randint(0, 100) # Simula uso da memório
        print(f"Uso de memória: {self.memory_usage}%")
        self.notify_observers() # Os observadores ficam "verificando o tempo todo"


    def run(self):
        while self.running:
            self.simulate_memory_usage()

# Exemplo de uso
if __name__ == "__main__":
    memory_monitor = MemorySubject(threshold=90) # Colocamos limiar de 90 para não deixar chegar a 100

    admins_notifier = GrupoEmailAdmins()
    users_notifier = GrupoEmailUsers()

    memory_monitor.add_observer(admins_notifier)
    memory_monitor.add_observer(users_notifier)

    memory_monitor.run()
