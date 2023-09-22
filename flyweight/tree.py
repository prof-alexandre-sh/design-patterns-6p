# Classe Flyweight para representar as características compartilhadas (intrinsic) de uma árvore
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def render(self, x, y):
        print(f"Renderizando uma árvore de tipo {self.name}, cor {self.color}, textura {self.texture} em ({x}, {y}).")

# Classe Flyweight Factory para gerenciar os tipos compartilhados
class TreeTypeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture) # Usamos um tupla (imutável) pra representar uma árvore única
        if key not in TreeTypeFactory._tree_types:
            TreeTypeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeTypeFactory._tree_types[key]

# Classe para representar uma árvore individual com características únicas
class Tree:
    def __init__(self, x, y, tree_type):
        # Características únicas
        self.x = x
        self.y = y

        # Característica compartilhada
        self.tree_type = tree_type 

    def render(self):
        self.tree_type.render(self.x, self.y)

# Função principal
if __name__ == "__main__":
    forest = []

    # Criar tipos de árvores compartilhados
    tree_type1 = TreeTypeFactory.get_tree_type("Carvalho", "Verde", "Rugosa")
    tree_type2 = TreeTypeFactory.get_tree_type("Bordo", "Vermelha", "Lisa")
    tree_type3 = TreeTypeFactory.get_tree_type("Bordo", "Vermelha", "Lisa")

    # Criar árvores individuais na floresta
    forest.append(Tree(1, 2, tree_type1))
    forest.append(Tree(3, 4, tree_type1))
    forest.append(Tree(5, 6, tree_type2))
    forest.append(Tree(7, 8, tree_type2))
    forest.append(Tree(9, 10, tree_type3)) # Aqui ele não cria um objeto novo. Reutiliza o que já existe

    # Renderizar as árvores
    for tree in forest:
        tree.render()

    print(len(TreeTypeFactory._tree_types))
