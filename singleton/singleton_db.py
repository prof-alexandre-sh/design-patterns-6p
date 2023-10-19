class DatabaseConnection:
    _instance = None
    
    '''
    cls para fazer referência a própria classe
    PEP 8:
        "Always use self for the first argument to instance methods."
        "Always use cls for the first argument to class methods."
    '''

    def __new__(cls):
        if cls._instance is None:
            # Super para chamar métodos da super classe
            # Nesse caso, passamos a própria DatabaseConnection
            # E chamamos um "novo __new__" para retornar um instância do seu tipo
            # Já estamos manipulando o  __new__ dessa classe, então usamos o super como estratégia para chamar um "novo __new__"
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Simular a inicialização da conexão com o banco de dados
            cls._instance.connect_to_database()
        return cls._instance

    def connect_to_database(self):
        self.db_connection = "Connected to the database"

    def execute_query(self, query):
        # Simular a execução de uma consulta no banco de dados
        print(f"Query '{query}' executed successfully")

# Uso:

# Duas instâncias da DatabaseConnection que deveriam ser a mesma instância.
db_instance1 = DatabaseConnection()
db_instance2 = DatabaseConnection()

# Verificando se são a mesma instância
print(db_instance1 is db_instance2)  # True

# Executar uma consulta na conexão com o banco de dados
db_instance1.execute_query("SELECT * FROM users")
