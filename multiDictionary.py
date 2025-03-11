import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.diz = None

    def printDic(self, language):
        if language == 'english':
            self.diz = d.Dictionary("resources/English.txt")
        elif language == 'italian':
            self.diz = d.Dictionary("resources/Italian.txt")
        elif language == 'spanish':
            self.diz = d.Dictionary("resources/Spanish.txt")
        else:
            print("problema nel metodo printDict")
        self.diz.printAll()

    def searchWord(self, words, language):
        lista = []
        listaRW = []

        if language == 'english':
            self.diz = d.Dictionary("resources/English.txt")
        elif language == 'italian':
            self.diz = d.Dictionary("resources/Italian.txt")
        elif language == 'spanish':
            self.diz = d.Dictionary("resources/Spanish.txt")
        else:
            print("problema nel metodo searchWord")

        lista = self.diz.listaParole
        if words and lista:
            for word in words:
                #print(word)
                parola = rw.RichWord(word)
                #print(parola)
                if word in lista:
                    #print(f"{parola} trovata nel dizionario e aggiunta all'elenco di rw")
                    listaRW.append(parola)
                    parola.corretta = True
                else:
                    #print(f"{parola} non trovata nel dizionario e aggiunta all'elenco di rw")
                    listaRW.append(parola)
                    parola.corretta = False
        return listaRW


