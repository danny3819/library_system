#it's does make library as object for make more in one instance
class Library:
    def __init__(self,name,books):
        self.books = books
        self.name = name
        self.lends_books = {}
    
    def show_books(self): #do show a view of the names books
        for e in self.books:
            print(f"{self.books.index(e)}.- {e}")
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

books = []#list of the books imported from file

with open("./libros.txt","r+") as f:#importing the books from file txt
    bs = f.readlines()
    for e in bs:
        books.append(e.strip())

Darien = Library("Darien",books)

counter = True #a system is made for show a menu
while counter:
    try:
        decition = int(input(f"\n hola escoje una opcion: \n{menu}\n>>>").strip())
    except:
        print("\n escribe solo numeros \n")
        break
    if decition == 1:
        Darien.show_books()
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
        