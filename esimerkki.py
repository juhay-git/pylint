# esimerkki.py

def add(a, b):
    return a+b

def subtract(a, b):
  return a-b

def multiply(a, b):
    return a * b
    print("Tätä ei koskaan tulosteta")  # Suorittamaton koodi

class OmaLuokka:
    def __init__(self, x):
        self.x = x

    def double_value(self):
        return self.x * 2
    
    def unused_method(self):
        pass

oma_muuttuja = 5

def unused_function():
    return "Tätä ei koskaan kutsuta"
