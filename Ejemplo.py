class Objeto():
	def __init__(self, forma, color):
		self.forma = forma
		self.color = color

	def transformar(self, nueva_forma):
		self.forma = nueva_forma

	def colorear(self, nuevo_color):
		self.color = nuevo_color

	def __str__(self):
		return "Forma: {} Color:{}".format(self.forma, self.color)

objeto1 = Objeto("cuadrado", "azul")
objeto2 = Objeto("triangulo", "amarillo")

objeto1.transformar("circulo")
objeto2.colorear("lila")

print(objeto1)
print(objeto2)
