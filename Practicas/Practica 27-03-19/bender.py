import math

# x = rsen(tetha)cos(fi)
# y = rsen(tetha)sen(fi)
# z = rcos(tetha)

# Inicio para +x
# tetha = 90
# fi = 0

class CoordCiruclar:
    def __init__(self):
        self.t = math.pi/2
        self.f = 0

    def gira(self, tipo):
        if (tipo == "+y"):
            self.f += math.pi/2
        elif (tipo == "-y"):
            self.f -= math.pi/2
        elif (tipo == "+z"):
            self.t -= math.pi/2
        elif (tipo == "-z"):
            self.t += math.pi/2

class Vector3:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def Max(self): 
        if(self.x == 1):
            return "+x" 
        if(self.x == -1):
            return "-x" 
        if(self.y == 1):
            return "+y"
        if(self.y == -1):
            return "-y"
        if(self.z == 1):
            return "+z"
        if(self.z == -1):
            return "-z" 
        
        return res

    def CalculaDir(self, angulos):
        self.x = math.sin(angulos.t) * math.cos(angulos.f)
        self.y = math.sin(angulos.t) * math.sin(angulos.f)
        self.z = math.cos(angulos.t)

def bend(dirs, num):
    a = CoordCiruclar()
    aux = num
    i = 1
    #for i in range(1, num+1):
    while(i < aux + 1):
        if(dirs[i] == "No"):
            dirs.pop(i)
            i -= 1
            aux -= 1
        i += 1
    num = aux
    if (num > 2):
        for i in range(1, num+1):
            for j in range (1, i+1):
                a.gira(dirs[j])
    else:
        for i in range(1, num+1):
            a.gira(dirs[i])
    v = Vector3()
    v.CalculaDir(a);
    return v.Max()
    


def main():
    #m = ["","+z", "+y", "+z"]
    #print(bend(m, 3))
    res = []
    num = 0
    while True:
        n = int(input())
        if n != 0:
            aux = input()
            a = aux.split()
            a.insert(0, "")
            res.append(bend(a, n-1))
            num += 1
        else:
            break
    for i in range(num):
        print(res[i])


main()