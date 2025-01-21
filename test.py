class User:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __add__(self, other: 'User'):
        return self.age + other.age