class pokemon:
  def __init__(self, nome, tipo, numero):
    self.nome = nome
    self.tipo = tipo
    self.numero = numero

  def get_nome(self):
      return self.nome
  def get_tipo(self):
      return self.tipo
  def get_numero(self):
      return self.numero
  def set_nome(self,nome):
      self.nome = nome
  def set_tipo(self,tipo):
      self.tipo = tipo
  def set_numero(self,numero):
      self.numero = numero

  def Mdados(self):
      print("nome: ",self.nome)
      print("Tipo: ",self.tipo)
      print("numero:",self.numero)

  def MD2(self):
      print("nome: ",self.get_nome())
      print("tipo: ",self.get_tipo())
      print("tipo: ",self.get_numero())

  def Rdados(self):

      dados = f'{self.nome},{self.tipo},{self.numero}'
      return dados

  def Tipo_especifico(self):

      if self.tipo == 'normal':
          print("É mais comun de se achar este tipo na região de Kanto!")
      if self.tipo == 'fogo':
          print("É mais comun de se achar este tipo na região de Kanto!")
      if self.tipo == 'fada':
          print("Mais Comum na região de Kalos")
      if self.tipo == 'eletrico':
          print("É mais comun de se achar este tipo na região de Kanto!")
      if self.tipo == 'psiquico':
          print("É mais comun de se achar em jotoh")
      if self.tipo == 'sombrio':
          print("É mais comun de se achar este tipo na região de Kalos!")

if __name__ =='__main__':
    pokemon1 = pokemon("Eevee", "normal", "133")
    pokemon2 = pokemon("Vaporeon", "agua", "134")
    pokemon3 = pokemon("Jolteon", "eletrico", "135")
    pokemon4 = pokemon("Flareon", "fogo", "136")
    pokemon5 = pokemon("Espeon", "psiquico", "196")
    pokemon6 = pokemon("Umbreon", "sombrio", "197")
    pokemon7 = pokemon("leafon", "grama", "470")
    pokemon8 = pokemon("Glaceon", "gelo", "471")
    pokemon9 = pokemon("Silveon", "fada", "700")

    ##Pokemon 1 Resultados
    print(' pokemon 1:', )
    print('Nome: ',pokemon1.get_nome())
    print('Tipo: ',pokemon1.get_tipo())
    print('Numero: ',pokemon1.get_numero())

    ##Pokemon 2 Rsultados
    print('pokemon 2:')
    print('Nome: ',pokemon2.get_nome())
    print("Tipo: ",pokemon2.get_tipo())
    print("Numero:",pokemon2.get_numero())

   ##Pokemon 3 Resultado
    print('pokemon 3:')
    print('Nome: ', pokemon3.get_nome())
    print("Tipo: ", pokemon3.get_tipo())
    print("Numero:", pokemon3.get_numero())

    ##Pokemon 4 Resultado
    print('pokemon 4:')
    print('Nome: ', pokemon4.get_nome())
    print("Tipo: ", pokemon4.get_tipo())
    print("Numero:", pokemon4.get_numero())

    ##Pokemon 5 Resultado
    print('pokemon 5:')
    print('Nome: ', pokemon5.get_nome())
    print("Tipo: ", pokemon5.get_tipo())
    print("Numero:", pokemon5.get_numero())

    ##Pokemon 6 Resultado
    print('pokemon 6:')
    print('Nome: ', pokemon6.get_nome())
    print("Tipo: ", pokemon6.get_tipo())
    print("Numero:", pokemon6.get_numero())

    ##Pokemon 7 Resultado
    print('pokemon 7:')
    print('Nome: ', pokemon7.get_nome())
    print("Tipo: ", pokemon7.get_tipo())
    print("Numero:", pokemon7.get_numero())

    ##Pokemon 8 Resultado
    print('pokemon 8:')
    print('Nome: ', pokemon8.get_nome())
    print("Tipo: ", pokemon8.get_tipo())
    print("Numero:", pokemon8.get_numero())

    ##Pokemon 9 Resultado
    print('pokemon 9:')
    print('Nome: ', pokemon9.get_nome())
    print("Tipo: ", pokemon9.get_tipo())
    print("Numero:", pokemon9.get_numero())
    ##regiões
    pokemon1.Tipo_especifico()
    pokemon2.Tipo_especifico()
    pokemon3.Tipo_especifico()
    pokemon4.Tipo_especifico()
    pokemon5.Tipo_especifico()
    pokemon6.Tipo_especifico()
    pokemon7.Tipo_especifico()
    pokemon8.Tipo_especifico()
    pokemon9.Tipo_especifico()