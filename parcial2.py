class Empresas:
  def __init__(self):
      self.nombre = ""
      self.nit = ""
      self.tipo_empresa = ""
      self.empleados = []
      self.edades = []
      self.genero = []
      self.es_cabeza_de_hogar = []
      self.nomina = []

  def crear_datos_iniciales(self):
      while True:
          self.nombre = input("Ingrese el nombre de la empresa: ")
          self.nit = input("Ingrese el NIT de la empresa (10 dígitos): ")

          if self.nombre == "" or len(self.nit) != 10:
              print("Error: El nombre y el NIT son obligatorios. El NIT debe tener 10 dígitos.")
              continue

          try:
              int(self.nit)  
          except ValueError:
              print("Error: El NIT debe ser un número.")
              continue

          break

  def ingresar_empleado(self):
      nombre = input("Ingrese el nombre completo del empleado: ")
      genero = input("Ingrese el género del empleado (M/F/O): ")
      es_cabeza_de_hogar = input("Ingrese si el empleado es cabeza de hogar (true/false): ")

      self.empleados.append(nombre)
      self.genero.append(genero)
      self.es_cabeza_de_hogar.append(es_cabeza_de_hogar)

      edad = int(input("Ingrese la edad del empleado: "))
      self.edades.append(edad)

      extra = 0
      if 20 <= edad <= 30:
          extra = 200000
      elif 30 <= edad <= 40:
          extra = 400000
      elif 40 <= edad <= 50:
          extra = 500000
      elif 50 <= edad <= 60:
          extra = 600000
      else:
          extra = 700000

      if es_cabeza_de_hogar.lower() == "true":
          extra *= 1.3

      if genero.upper() == "F":
          extra *= 1.1

      salario_base = 1160000
      total = salario_base + extra

      self.nomina.append(total)

  def mujeres(self):
      return [empleado for empleado, gender in zip(self.empleados, self.genero) if gender.upper() == "F"]


empresa = Empresas()
empresa.crear_datos_iniciales()

empresa2 = Empresas()
empresa2.crear_datos_iniciales()

empresa3 = Empresas()
empresa3.crear_datos_iniciales()

# Numero de empleados
for _ in range(4):
  empresa.ingresar_empleado()

for _ in range(4):
  empresa2.ingresar_empleado()

for _ in range(4):
  empresa3.ingresar_empleado()
# Resultados
print("Nombre de la empresa #1:", empresa.nombre)
print("NIT de la empresa #1:", empresa.nit)
print("Empleados #1:", empresa.empleados)
print("Edades #1:", empresa.edades)
print("Género #1:", empresa.genero)
print("Es cabeza de hogar #1:", empresa.es_cabeza_de_hogar)
print("Nómina #1:", empresa.nomina)
print("Mujeres en la empresa #1:", empresa.mujeres())

#Empresa 2
# Resultados
print("Nombre de la empresa #2:", empresa2.nombre)
print("NIT de la empresa #2:", empresa2.nit)
print("Empleados #2:", empresa2.empleados)
print("Edades #2:", empresa2.edades)
print("Género #2:", empresa2.genero)
print("Es cabeza de hogar #2:", empresa2.es_cabeza_de_hogar)
print("Nómina #2:", empresa2.nomina)
print("Mujeres en la empresa #2:", empresa2.mujeres())

#Empresa 3
# Resultados
print("Nombre de la empresa #3:", empresa3.nombre)
print("NIT de la empresa #3:", empresa3.nit)
print("Empleados #3:", empresa3.empleados)
print("Edades #3:", empresa3.edades)
print("Género #3:", empresa3.genero)
print("Es cabeza de hogar #3:", empresa3.es_cabeza_de_hogar)
print("Nómina #3:", empresa3.nomina)
print("Mujeres en la empresa #3:", empresa3.mujeres())
