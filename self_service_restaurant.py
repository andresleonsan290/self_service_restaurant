### Restaurante auto servicio
## Authors:

# Andrés León
# Juan David Montenegro
# Juan José Sánchez Mora
# Oscar Javier Saavedra

## Se definen los precios totales de lo que valdrían todos los productos de cada categoría
total_prices = {
  "vegetables": 125000,
  "meats": 294000,
  "flours": 150000,
  "fruits": 60000,
  "pops": 70000
}

## Se definen los productos disponibles por categoría
#Todos los valores se inicializan en None para luego setear los precios con ciclos dependiendo del precio total
#declarado en el anterior diccionario
vegetables = {
  "pepino": None, "tomate": None, "lechuga": None, "apio": None, "aguacate": None
}
meats = {
  "res": None, "pollo": None, "cerdo": None, "cuy": None, "pavo": None, "chiguiro": None
}
flours = {
  "papa": None, "arroz": None, "yuca": None, "frijol": None, "lenteja": None, "ñame": None
}
fruits = {
  "pera": None, "piña": None, "banano": None, "manzana": None, "sandia": None, "melon": None
}
pops = {
  "sprite": None, "7up": None, "uva": None, "pepsi": None, "ginger": None, "kola": None, "te": None
}

order = {}

## Se añade la función encargada de verificar si el usuario ingresó lo que debe ingresar,
##Limpia el array que ingresa el usuario de espacios vacios y texto.
def checkOrder(dict, categoryOrdersList):
  cleanedCategoryOrdersList = []

#Se limpia el array
  for item in categoryOrdersList:
    try:
      if int(item) - 1 not in cleanedCategoryOrdersList:
        cleanedCategoryOrdersList.append(int(item) - 1)
    except:
      pass
  categoryOrdersList = cleanedCategoryOrdersList
  categoryOrdersListToReturn = list(categoryOrdersList)

## Se recorren los índices de los productos que eligió el usuario
  for order in categoryOrdersList:

## Descartar números que no pertenecen a ningún producto
    if(order < 0 or order >= len(dict.keys())):
      print("\033[1;33m"+ "El número " + str(order + 1) + " No pertenece a ningún producto" +'\033[') 
      categoryOrdersListToReturn.remove(order)

## Verificar si el array resultante luego de limpiado y de filtrado contiene mínimo 2 elementos
  if(len(categoryOrdersListToReturn) < 2):
    ## Si hay menos de 2 elementos en el array resultante, se ejecuta eso, se le pedirá al usuario nuevamente los productos y se volverá a llamar esta función de manera recursiva
    print("\033[1;36m"+ "Debes elegir mínimo dos productos, vuelve a ingresar los números correspondientes a los productos" +"\033[")
    categoryOrdersList = input().strip().split(' ')
    return checkOrder(dict, categoryOrdersList)
  else:
    ## Cuando hayan mínimo 2 productos seleccionados correctamente, se retornará la lista de índices de los productos de la categoría que el usuario seleccionó
    return categoryOrdersListToReturn

## Se define la función que añadirá al diccionario order, las ordenes que haga el usuario en cada categoría
def addOrder(dict, categoryOrdersList, categoryName):
  categoryOrdersList = checkOrder(dict, categoryOrdersList)

  ## Se declara la key de la categoría en cuestión en el diccionario order
  order[categoryName] = {}

  ## Se rellena la key de la categoría en el diccionario order, con los productos elegidos
  for productIndex in categoryOrdersList:
    order[categoryName][list(dict.keys())[productIndex]] = dict[list(dict.keys())[productIndex]]
  

### Se da la bienvenida al usuario
username = input('¿Cómo te llamas?\n').strip()
print("¡Hola " + username + "! Bienvenido a este restaurante auto servicio\n¿Qué deseas pedir?")
print("\033[1;36m"+ "- - - - - - - - - - - -" +"\033[")

## Se empiezan a mostrar los vegetales
print("Tenemos disponibles los siguientes 🥬vegetales")

## Ciclo encargado de rellenar precios en el diccionario vegetables
## Y de mostrar un listado al usuario de los vegetales disponibles
for key in vegetables.keys():
  vegetables[key] = total_prices["vegetables"] / len(vegetables)
#Se muestra el lstado de vegetales
  print("\033[1;32m"+ str(list(vegetables).index(key) + 1) + ".) " + key +'\033[')

## Se le pide al usuario qué vegetales quiere
vegetable_orders = input('Ingresa los números de los vegetables que quieres separados por un espacio, (mínimo 2)\n').strip().split(' ')
addOrder(vegetables, vegetable_orders, "Vegetales")
  

## Se empiezan a mostrar las carnes
print("Tenemos disponibles las siguientes 🥩Carnes")

## Ciclo encargado de rellenar precios en el diccionario meats
## Y de mostrar un listado al usuario de las carnes disponibles
for key in meats.keys():
  meats[key] = total_prices["meats"] / len(meats)
#Se muestra el listado de carnes
  print("\033[1;35m"+ str(list(meats).index(key) + 1) + ".) " + key +'\033[')

## Se le pide al usuario qué carnes quiere
meat_orders = input('Ingresa los números de las carnes que quieres separados por un espacio, (mínimo 2)\n').strip().split(' ')
addOrder(meats, meat_orders, "Carnes")


## Se empiezan a mostrar las harinas
print("Tenemos disponibles las siguientes 🍞harinas")

## Ciclo encargado de rellenar precios en el diccionario flours
## Y de mostrar un listado al usuario de las harinas disponibles
for key in flours.keys():
  flours[key] = total_prices["flours"] / len(flours)
#Se muestra el listado de harinas
  print("\033[1;37m"+ str(list(flours).index(key) + 1) + ".) " + key +'\033[')

## Se le pide al usuario qué harinas quiere
flour_orders = input('Ingresa los números de las Harinas que quieres separados por un espacio, (mínimo 2)\n').strip().split(' ')
addOrder(flours, flour_orders, "Harinas")


## Se empiezan a mostrar las frutas
print("Tenemos disponibles las siguientes 🍒frutas")

## Ciclo encargado de rellenar precios en el diccionario fruits
## Y de mostrar un listado al usuario de las frutas disponibles
for key in fruits.keys():
  fruits[key] = total_prices["fruits"] / len(fruits)
#Se muestra el listado de frutas
  print("\033[1;31m"+ str(list(fruits).index(key) + 1) + ".) " + key +'\033[')

## Se le pide al usuario qué frutas quiere
fruit_orders = input('Ingresa los números de las frutas que quieres separados por un espacio, (mínimo 2)\n').strip().split(' ')
addOrder(fruits, fruit_orders, "Frutas")


## Se empiezan a mostrar las bebidas
print("Tenemos disponibles las siguientes 🍹bebidas")

## Ciclo encargado de rellenar precios en el diccionario pops
## Y de mostrar un listado al usuario de las bebidas disponibles
for key in pops.keys():
  pops[key] = total_prices["pops"] / len(pops)
#Se muestra el listado de bebidas
  print("\033[1;34m"+ str(list(pops).index(key) + 1) + ".) " + key +'\033[')

## Se le pide al usuario qué bebidas quiere
pop_orders = input('Ingresa los números de las bebidas que quieres separados por un espacio, (mínimo 2)\n').strip().split(' ')
addOrder(pops, pop_orders, "Bebidas")

###Hallar totales y promedios
#
#Se definen las variables usadas para el total a pagar y el total de productos a adquirir
totalToPay = 0
productsQuantity = 0

## Se recorre el diccionario order para transportarnos entre categorías
for category in order:
  #Se define la variable usada para llevar la cuenta de la sumatorias de las categorías
  categorySumatory = 0

  #Se recorren los productos por cada categoría
  for product in order[category]:
    categorySumatory += order[category][product]

  #Se muestra el total de la categoría en cuestión redondeada en las centenas
  print("El precio total de la categoría (" + category + ") es de $" + str(round(categorySumatory/100) * 100) + " Por la compra de " + str(len(order[category])) + " " + category)
  
  #Se van sumando los totales de cada categoría para llegar al total de todo
  totalToPay += categorySumatory

  #Se van sumando los tamaños de las categorías para llegar a la cantidad total de productos a adquirir
  productsQuantity += len(order[category])

## Se muestra el valor total a pagar
print("El total a pagar es de $" + str(round(totalToPay/100) * 100) + " Por la compra de " + str(productsQuantity) + " productos")

## Se muestra el promedio de coste por cada producto
print("El promedio de precio de cada producto es de $" + str(round((totalToPay / productsQuantity)/100) * 100))