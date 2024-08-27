class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = vizinhos[:2]  # Máximo 2 vizinhos
        self.horas_alimentacao = horas_alimentacao

    def fazer_barulho(self):
        return f"{self.nome} faz '{self.barulho}'."

    def mover(self):
        return f"{self.nome} se move {self.movimento}."

    def alimentar(self):
        return f"{self.nome} foi alimentado às {self.horas_alimentacao}."

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Habitat: {self.habitat}, Vizinhos: {', '.join(self.vizinhos)}"


class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, tipo_pelo):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
        self.tipo_pelo = tipo_pelo


class Ave(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, cor_penas):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
        self.cor_penas = cor_penas


class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, tipo_pele):
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
        self.tipo_pele = tipo_pele


# Lista de animais cadastrados
zoologico = []

# Função para cadastrar novos animais
def cadastrar_animal():
    nome = input("Nome do animal: ")
    idade = int(input("Idade do animal: "))
    barulho = input("Som característico: ")
    movimento = input("Forma de locomoção: ")
    alimentacao = input("Dieta do animal: ")
    habitat = input("Habitat natural: ")
    vizinhos = input("Nomes dos vizinhos (separados por vírgula, máximo 2): ").split(',')[:2]
    horas_alimentacao = input("Horário de alimentação: ")

    print("Categoria do animal:\n1. Mamífero\n2. Ave\n3. Réptil")
    categoria = int(input("Escolha a categoria: "))

    if categoria == 1:
        tipo_pelo = input("Tipo de pelo: ")
        animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, tipo_pelo)
    elif categoria == 2:
        cor_penas = input("Cor das penas: ")
        animal = Ave(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, cor_penas)
    elif categoria == 3:
        tipo_pele = input("Tipo de pele: ")
        animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao, tipo_pele)
    else:
        print("Categoria inválida!")
        return

    zoologico.append(animal)
    print(f"{nome} foi cadastrado com sucesso!")

# Função para listar todos os animais
def listar_animais():
    for animal in zoologico:
        print(animal)

# Função para buscar um animal por nome
def buscar_animal():
    nome = input("Digite o nome do animal que deseja buscar: ")
    for animal in zoologico:
        if animal.nome == nome:
            print(animal)
            return
    print("Animal não encontrado.")

# Função para listar animais por categoria
def listar_por_categoria():
    print("Escolha a categoria:\n1. Mamífero\n2. Ave\n3. Réptil")
    categoria = int(input("Categoria: "))

    for animal in zoologico:
        if categoria == 1 and isinstance(animal, Mamifero):
            print(animal)
        elif categoria == 2 and isinstance(animal, Ave):
            print(animal)
        elif categoria == 3 and isinstance(animal, Reptil):
            print(animal)

# Função para listar vizinhos de um animal
def listar_vizinhos():
    nome = input("Digite o nome do animal para ver os vizinhos: ")
    for animal in zoologico:
        if animal.nome == nome:
            print(f"Vizinhos de {nome}: {', '.join(animal.vizinhos)}")
            return
    print("Animal não encontrado.")

# Função para simular a alimentação dos animais
def simular_alimentacao():
    for animal in zoologico:
        print(animal.alimentar())

# Menu principal
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo animal")
        print("2. Listar todos os animais")
        print("3. Buscar animal por nome")
        print("4. Listar animais por categoria")
        print("5. Listar vizinhos de um animal")
        print("6. Simular alimentação")
        print("7. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_animal()
        elif opcao == 2:
            listar_animais()
        elif opcao == 3:
            buscar_animal()
        elif opcao == 4:
            listar_por_categoria()
        elif opcao == 5:
            listar_vizinhos()
        elif opcao == 6:
            simular_alimentacao()
        elif opcao == 7:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Cadastro inicial de animais
zoologico.append(Mamifero("Leão", 5, "Rugido", "em 4 patas", "Carnívoro", "Savana", ["Tigre"], "12:00"))
zoologico.append(Ave("Águia", 3, "Grito", "Voando", "Carnívoro", "Montanhas", ["Coruja"], "08:00"))
zoologico.append(Reptil("Cobra", 2, "Sibilo", "Rastejando", "Carnívoro", "Florestas", ["Tartaruga"], "14:00"))
zoologico.append(Mamifero("Elefante", 10, "Trumpete", "em 4 patas", "Herbívoro", "Savanas", ["Leão"], "13:00"))
zoologico.append(Ave("Coruja", 4, "Assobio", "Voando", "Carnívoro", "Florestas", ["Águia"], "09:00"))
zoologico.append(Reptil("Tartaruga", 100, "Silêncio", "Caminhando", "Herbívoro", "Praias", ["Cobra"], "11:00"))
zoologico.append(Reptil("Trionyx", 8, "Rugido", "Teletransportar", "Pesadelos", "Rio dos sinos", ["lindomar"], "13:00")

if __name__ == menu():
    menu()
