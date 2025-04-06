#it's does make library as object for make more in one instance
class library:
    def __init__(self,name,books):
        self.books = books
        self.name = name
        self.lends_books = {}
    
    def show_books(self): #do show a view of the names books
        pass
    def lend_book(self):
        pass
    def add_book(self):
        pass
    def delete_book(self):
        pass
    def show_lend(self):
        pass

menu = """
1.-ver libros
2.-prestar un libro
3.-agregar libro
4.-eliminar un libro
5.-mostrar prestados
99.-salir"""

counter = True #a system is made for show a menu
while counter:
    try:
        decition = int(input(f"hola escoje una opcion: \n{menu}\n>>>").strip())
    except:
        print("\n escribe solo numeros \n")
        break
    if decition == 1:
        pass
    elif decition == 2:
        pass
    elif decition == 3:
        pass
    elif decition == 4:
        pass
    elif decition == 5:
        pass
    elif decition == 99:
        counter = False
    else:
        print("entrada invalida")
        