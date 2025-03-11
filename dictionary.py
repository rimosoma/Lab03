import resources

class Dictionary:
    def __init__(self, path):
        self.path = path
        self.listaParole = []
        self.loadDictionary(self.path)


    def loadDictionary(self,path):
        try:
            with open(path) as f:
                for line in f:
                    parola = line.strip()
                    self.listaParole.append(parola)
        except FileNotFoundError:
            print(f"File called {path}not found")
        except Exception as e:
            print(f"Error in loadDictionary: {e}")

    def printAll(self):
        for parola in self.listaParole:
            print(parola+"\n")


    @property
    def _list(self):
        return self.listaParole