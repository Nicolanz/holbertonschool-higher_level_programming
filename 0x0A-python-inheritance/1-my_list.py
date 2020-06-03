#!usr/bin/python3
class MyList(list):
    def print_sorted(self):
        lista = self.copy()
        lista.sort()
        print(lista)
