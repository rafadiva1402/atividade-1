# sistema_funcionarios.py

# Classe base
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario}")

    def executar_tarefa(self):
        print("Executando tarefa genérica de funcionário.")

# Subclasse - Desenvolvedor
class Desenvolvedor(Funcionario):
    def executar_tarefa(self):
        print(f"{self.nome} está programando em Python.")

# Subclasse - Designer
class Designer(Funcionario):
    def executar_tarefa(self):
        print(f"{self.nome} está criando um layout no Figma.")

# Subclasse - Gerente
class Gerente(Funcionario):
    def executar_tarefa(self):
        print(f"{self.nome} está coordenando a equipe de projeto.")

# Subclasse - Estagiário
class Estagiario(Funcionario):
    def executar_tarefa(self):
        print(f"{self.nome} está aprendendo e auxiliando a equipe.")

# Testando
funcionarios = [
    Desenvolvedor("Alice", 7000),
    Designer("Bruno", 6000),
    Gerente("Carla", 10000),
    Estagiario("Daniel", 1500)
]

for f in funcionarios:
    f.exibir_informacoes()
    f.executar_tarefa()
    print("-" * 30)
