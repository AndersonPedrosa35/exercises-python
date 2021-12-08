class Area_do_retangulo:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
      print(f"A area total do quadrado é {self.lado ** 2 }")


retangulo = Area_do_retangulo(4)
retangulo.area()