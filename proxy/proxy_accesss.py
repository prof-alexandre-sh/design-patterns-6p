'''
Neste exemplo, temos um sistema de permissões de acesso representado pela interface UserService. 
A classe RealUserService é a implementação concreta desse serviço e é responsável por conceder ou negar 
o acesso com base no usuário autenticado.

O proxy é representado pela classe PermissionProxy. 
Ele controla o acesso ao serviço real e verifica se o usuário que está solicitando o acesso é o mesmo 
que foi autenticado anteriormente. Se o usuário for o mesmo, o proxy permite o acesso e encaminha a 
solicitação para o serviço real. Caso contrário, nega o acesso.

Isso é útil em cenários de autenticação e autorização, onde desejamos controlar o acesso a recursos 
com base nas permissões do usuário autenticado. 
O proxy atua como um intermediário que adiciona uma camada de controle de acesso ao serviço real.
'''

# Interface para o objeto real
class UserService:
    def access_granted(self, user):
        pass

# Classe RealSubject
class RealUserService(UserService):
    def access_granted(self, user):
        return f"Acesso concedido para o usuário {user}"

# Proxy
class PermissionProxy(UserService):
    def __init__(self, user, real_user_service):
        self.user = user
        self.real_user_service = real_user_service

    def access_granted(self, user):
        if user == self.user:
            return self.real_user_service.access_granted(user)
        else:
            return "Acesso negado"

# Cliente
if __name__ == "__main__":
    real_user_service = RealUserService()
    proxy = PermissionProxy("João", real_user_service)

    # Usuário autenticado
    print(proxy.access_granted("João"))  # Acesso concedido para o usuário João

    # Usuário não autenticado
    print(proxy.access_granted("Maria"))  # Acesso negado