# Classe que realiza migrações para uma máquina virtual
class MigraSolucao:
    def migrate_to_vm(self, aplicacao):
        print("Migrando credenciais...")
        print("Migrando BD...")
        print("Migrando código...")

# Interface alvo para migrações para Kubernetes
class MigraKubernetesInterface:
    def migrate_to_kubernetes(self, aplicacao):
        pass

# Adaptador para realizar migrações para Kubernetes usando MigraSolucao
class Adaptador(MigraKubernetesInterface):
    def __init__(self, migrator):
        self.migrator = migrator

    def migrate_to_kubernetes(self, aplicacao):
        print(f"Adaptando o método de migração para publicar a apĺicação {aplicacao} no kubernetes...")
        self.migrator.migrate_to_vm(aplicacao)  # Redirecionar para a migração para VM
        print("Publicando no cluster...")

# Classe concreta que realiza migrações para Kubernetes
class MigraKubernetes(MigraKubernetesInterface):
    def migrate_to_kubernetes(self, aplicacao):
        print(f"Migrating code '{aplicacao}' to Kubernetes")

# Criando uma instância da classe MigraSolucao
migrator = MigraSolucao()

# Criando uma instância do adaptador para migrações para Kubernetes
kubernetes_adapter = Adaptador(migrator)

# Criando uma instância da classe MigraKubernetes
real_kubernetes_migrator = MigraKubernetes()

# Executando as migrações
aplicacao = "some_code"
kubernetes_adapter.migrate_to_kubernetes(aplicacao)  # Usando o adaptador para migração para Kubernetes
#real_kubernetes_migrator.migrate_to_kubernetes(aplicacao)  # Usando a classe concreta para migração para Kubernetes