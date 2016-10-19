import random
MAX_IN = 5
MAX_OUT = 5
MAX_NOT = 5
AVAIL_OPS=60
MAX_OPS = 8

NOT=-1
AND = -2
OR = -3
XOR = -4
NAND = -5
NOR = -6
IMP = -7

class t_scheme:
    array = []
    works = True
    nots = 0
    ops = 0
    ins = 0
    exts = 0
    unused = set()
    def add(self,ty,i0,i1,ou):
        """Добавить кортеж в таблицу"""
        self.array.append({'type':ty,'in0':i0,'in1':i1,'out':ou,'used':False})
        self.unused.add(ou)

    def __init__(self):
       for i in range(MAX_IN):
           self.add(i,i,i,i)
           self.ins=self.ins+1
    def write(self):
        print("T_scheme:")
        print("     Elements:")
        for x in self.array:
            print(x)
        print("     Works:   ",self.works)
        print("     NotS:    ",self.nots)
        print("     Ops:     ",self.ops)
        print("     Ins:     ",self.ins)
        print("     Exts:    ",self.exts)
        print("     Unused:  ",self.unused)
    def add_rand(self):
        op = -random.randint(1,7)
        #Добавить поддержку множеств. Что добавлять в множества?
        if (self.ops >=AVAIL_OPS *2/3) and len(self.unused)>=MAX_OUT:
            in0 = random.choice(list(self.unused))
            in1 = 0 + in0
            while in1 == in0:
                in1 = random.choice(list(self.unused))

        else:
            in0 = random.randint(0,self.ins-1) #Первый вход
            in1 = random.randint(0,self.ins-1) #Второй вход для бинарных
        self.array[in0]['used']=True
        if op != NOT:
            self.add(op,in0,in1,self.ins)
            self.ins = self.ins +1
        else:
            self.array[in1]['used']=True
            self.add(op,in0,None,self.ins)
            self.ins = self.ins +1
            self.nots=self.nots+1
        self.unused=self.unused - {in0}
        self.unused = self.unused - {in1}
        self.ops=self.ops+1

if __name__ == "__main__":
    a=t_scheme()
    while a.ops <= AVAIL_OPS:
        a.add_rand();
    a.write()









