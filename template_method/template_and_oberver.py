from abc import ABC, abstractmethod
import random

# Classe abstrata que define o Observador
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

## Refatorado
# Classe concreta que implementa o Observador
class GrupoEmailAdmins(Observer):

    def update(self, sujeito): 
        print(f"Enviando e-mail para Admins: {sujeito.error_message}") # Notifica todos e mata processo
        print(f"Ação: {sujeito.action}")
        

## Refatorado
# Classe concreta que implementa o Observador
class GrupoEmailUsers(Observer):

    def update(self, sujeito):
        print(f"Enviando email para usuários: {sujeito.error_message}") # Apenas notifica grupo de usuários
        print(f"Ação: {sujeito.action}")

## Refatorado
class Cluster:
    def __init__(self):
        self.observers = {}
        self.memory_usage = 0  # Simulando a utilização de memória
        self.threshold = 90  # Limite de memória antes da notificação
        self.running = True
        self.error_message = ''
        self.action = ''

    ## ---------- Método padrão ----------
    def add_observer(self, name, observer):
        self.observers[name] = observer

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        # Lógica de notificação é delegada para a classe template
        if self.memory_usage >= self.threshold:
            self.observers["users"].update(self)
            self.observers["admins"].update(self)
        elif self.memory_usage >= 70:
            self.observers["users"].update(self)

    ## ---------- Métodos abstratos ----------

    @abstractmethod
    def set_error_message(self):
        pass

    @abstractmethod
    def set_action(self):
        pass

    ## ---------- Template method ----------
    @abstractmethod
    def simulate_memory_usage(self):
        self.memory_usage = random.randint(0, 100) # Simula uso da memório
        print(f"Uso de memória: {self.memory_usage}%")
        self.set_error_message()
        self.set_action()
        self.notify_observers() # Os observadores ficam "verificando o tempo todo"

    ## ---------- Método padrão ----------
    def run(self):
        while self.running:
            self.simulate_memory_usage()
            if self.memory_usage >= self.threshold:
                self.running = False # A definição do status de execução faz mais sentido no contexto dessa função run

## Refatorado
class ClusterCronJobs(Cluster):

    def set_error_message(self):
        self.error_message = "OOMKILL!"

    def set_action(self):
        self.action = "Preparando para parar cluster"

## Refatorado            
class ClusterApis(Cluster):

    def set_error_message(self):
        self.error_message = "Request denied! Memory allocation error"

    def set_action(self):
        self.action = "Não fazer mais requisições! Aguardar finalização dos requests na fila!"

# Exemplo de uso
if __name__ == "__main__":

    crons_cluster = ClusterCronJobs() # Cluster de cronjobs
    apis_cluster = ClusterApis() # Cluster de apis

    admins_notifier = GrupoEmailAdmins() # Assinante admins
    users_notifier = GrupoEmailUsers() # Assinante usuários

    crons_cluster.add_observer("admins", admins_notifier)
    crons_cluster.add_observer("users", users_notifier)

    apis_cluster.add_observer("admins", admins_notifier)
    apis_cluster.add_observer("users", users_notifier)

    #crons_cluster.run()
    apis_cluster.run()
