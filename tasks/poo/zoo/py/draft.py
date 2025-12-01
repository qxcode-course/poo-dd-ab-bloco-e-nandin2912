from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")   



    @abstractmethod
    def fazer_som(self):
        pass



    @abstractmethod
    def mover(self):
        pass


class Leao(Animal):  
    def __init__(self, nome: str):
        super().__init__(nome)        

    def fazer_som(self):
        print(" rugido!")

    def mover(self):
        print("o leao está correndo.")



class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)


    def fazer_som(self):
        print("bramido!")

    def mover(self):
        print ("o elefante esta caminhando lentamente.")


class Cobra(Animal):

    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("sssss")

    def mover(self):
        print("a cobra esta rastejando.")

def apresentar(animal:  Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print("tipo: ", type(animal).__name__)
    print()


animais = [
    Leao("Leão africano"),
    Elefante("Elefante da asia"),
    Cobra("Cobra naja")
]    

for a in animais:
    apresentar(a)



                                   
