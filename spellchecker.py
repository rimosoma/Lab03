import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.database = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~?"
        for c in chars:
            txtIn = txtIn.replace(c,"")
        txtIn = txtIn.replace("'"," ")
        words = txtIn.lower().split()
        listaParoleInput = self.database.searchWord(words,language)


        contoErrate = 0
        listaParoleErrate = []
        for rw in listaParoleInput:
            if rw.corretta == False:
                contoErrate +=1
                listaParoleErrate.append(rw)

        print(f"numero parole errate = {contoErrate}")
        for rw in listaParoleErrate:
            print(rw)
        print(f"tempo impiegato per l'operazione : {time.process_time()}")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

