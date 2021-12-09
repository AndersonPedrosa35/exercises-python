class television:
    def __init__(self, tamanho):
      self.volume = 50
      self.canal = 1
      self.tamanho = tamanho
      self.ligada = False
    
    def aumentar_volume(self):
        if self.volume < 99:
            self.volume += 1  
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def modificar_canal(self, canal):
        if 0 < canal < 99:
            self.canal = canal
        else:
            raise ValueError

    def liga_desligar(self):
        self.ligada = not self.ligada


class OperationsAritmeticas:
    def __init__(self, list_numbers):
        if type(list_numbers) is list or type(list_numbers) is tuple:
            self.list_numbers = list_numbers
        else:
            raise ValueError
    
    def media(self):
        total = 0
        for number in self.list_numbers:
            total += number
        return total / len(self.list_numbers)

    def mediana(self):
        tamanho = len(self.list_numbers)
        meio = tamanho / 2
        if (meio != int):
            pass

    def moda(self):
        repeat_number = {}
        number_max = 0
        for number in self.list_numbers:
            repeat_number[number] = 0
            for repeat in self.list_numbers:
                if number == repeat:
                    repeat_number[number] += 1
        for key in repeat_number:
            if repeat_number[key] > number_max:
                number_max = key
        return number_max


numbers = OperationsAritmeticas([1, 2, 3, 4, 5, 5, 6])
print(vars(numbers))
print(numbers.media())
print(numbers.moda())