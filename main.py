import json #Importamos JSON

"""--------------------------------------------------------------------------"""

with open("ruta") as f: #Para leer JSON
    json.load(f)        #F es el archivo que queremos leer

"""--------------------------------------------------------------------------"""

variable = "Tunometecabrasaramambiche" #Creamos variable de lo que querramos escribir
with open("ruta","w") as f: # Para escribir usamos "W"(borra) o "A"(añade)
    json.dump(variable,f) #Lo dumpeamos de esta manera:(Variable anterior, destino)

"""--------------------------------------------------------------------------"""

with open("ruta") as f: #Para leer cualquier archivo

    f.read()            #Leemos todo en un solo string
    f.readline()        #Leemos una linea a la vez(Podemos usar .seek()
    f.readlines()       #Leemos una lista donde cada linea es un elemento

"""--------------------------------------------------------------------------"""

with open("ruta","w") as f: #Para escribir cualquier archivo

    f.write("Pito")         #Toma un solo valor a la vez, simplemente
#                            lo ponemos entre los parentesis
