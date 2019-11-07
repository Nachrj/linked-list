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
        ultimo = str(self.ult)
        if index is not None:
            if int(self.len) < index:
                raise IndexError("Index out of range")
        else:
            currentNext = self.prim.next
            current = self.prim
            while currentNext is not self.ult:
                current = current.next
                print(str(currentNext))
                currentNext = currentNext.next
            self.ult = current
            self.ult.prox = None
        return str(ultimo)
    
    def index(self,elem): 
        current = self.prim
        ix = 0
        for i in range(self.len):
            if current is elem:
                return ix          
            current = current.next
            ix += 1
        return None
    
    def insert(self,index,elem): 
        if self.len < index :
            raise IndexError("Index out of range")
        return
    
    def remove(self, elem): 
        return 
    
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

Lista = ListaEnlazada()
Lista.append("Nacho")
Lista.append("Bruno")
Lista.append("Manu")