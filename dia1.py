class User:
    def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password

    def qual_o_seu_nome(self):
      return self.name


minha_primeira_class = User("Anderson", "anderson@gmail.com", "123")
meu_primeiro_metodo = minha_primeira_class.qual_o_seu_nome()

print(User)
print(minha_primeira_class.email)
print(meu_primeiro_metodo)