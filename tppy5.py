class Nodo:
    def __init__(self, v=None,prox=None):
        self.v=v
        self.next=prox
        
    def __str__(self):
        return self.v
    
class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.ult = None
        self.len = 0
        
    def pop(self, index=None):
        ultimo = self.ult
        AntCurrent = self.prim
        current = AntCurrent.next
        i = 1
        if index is not None:
            if int(self.len) <= index:
                raise IndexError("Index out of range")
            while current is not None:
                if index == 0:
                        borra3 = AntCurrent
                        self.prim = AntCurrent.next
                        self.len -= 1
                        return borra3
                if i == index:
                    if current.next is None:
                        borra = current
                        self.ult = AntCurrent
                        AntCurrent.next = None
                        self.len -= 1
                        return borra
                    borrado = current
                    AntCurrent.next = current.next #ESTO ESTA MAL
                    self.len -= 1
                    return borrado
                i += 1
                AntCurrent = AntCurrent.next
                current = current.next
        else:
            while current.next is not None:
                AntCurrent = AntCurrent.next
                current = current.next
            self.ult = AntCurrent
            self.ult.next = None
            self.len -= 1
        return ultimo
    
    def index(self,elem): 
        current = self.prim
        ix = 0
        for i in range(self.len):
            if current.v == elem:
                return ix          
            current = current.next
            ix += 1
        return 
    
    def insert(self,index,elem): 
        if self.len < index :
            raise IndexError("Index out of range")
        return
    
    def remove(self, elem): 
        AntCurrent = self.prim
        current = self.prim.next
        if AntCurrent.v == elem:
            self.prim = current
            self.len -= 1
            return
        while current is not None:
            if current.v == elem:
                if current.next is None:
                    self.ult = AntCurrent
                AntCurrent.next = current.next
                self.len -= 1
                return
            AntCurrent = AntCurrent.next
            current = current.next
        raise ValueError
    
    def append(self,elem): 
        if self.prim is None:
            self.prim = Nodo(elem)
            self.len += 1
            return
        else:
            self.len += 1
            self.ult = Nodo(elem)
        current = self.prim
        while current.next is not None:
            current = current.next
        current.next = Nodo(elem)
        return
    
    def __len__(self):
        return self.len
    
    def __str__(self): 
       l = []
       current=self.prim
       for i in range(self.len):
           l.append(current.v)
           current=current.next
       return str(l)

if __name__ == "__main__":
    Lista = ListaEnlazada()
    Lista.append("Nacho")
    Lista.append("Bruno")
    Lista.append("Manu")
    Lista.append("Fede")
    print(Lista)