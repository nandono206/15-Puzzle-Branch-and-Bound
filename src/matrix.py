import copy

class Matrix:
    #Konstruktor Kelas
    def __init__(self, source):
        self.arr = source
        #jika dibuat di awal(dari file)
        try:
            self.arr = []
            f = open("../test/"+source , "r")
            for line in f:
                self.arr.append(list(map(lambda x : int(x), line.split())))
        #jika dibuat dari pergerakan state sebelumnya
        except:
            self.arr = source

    def calculateCost(self):
        temp = self.toOneDim()
        misplaced = 0

        for i in range(16):
            #jika bukan 16 periksa apakah sudah benar posisinya
            if temp[i] != 16 and temp[i] != i+1:
                misplaced += 1
        
        return misplaced     

    def printMatrix(self):
        for row in self.arr:
            for elem in row:
                if elem == 16:
                    elem = '#'
                print('%4s' % elem, end="")
            print()

    def toOneDim(self):
        temp = []
        for row in self.arr:
            for elem in row:
                temp.append(elem)
        return temp

    def cekKurang(self):
        temp = self.toOneDim()
        kurang = 0
        for i in range(16):
            for j in range(i+1,16):
                if temp[j] < temp[i]:
                    kurang+=1
        return kurang

    def findEmptySlot(self):
        for i in range(4):
            for j in range(4):
                if self.arr[i][j] == 16:
                    return (i, j)

    def cekSolvabilitas(self):
        kurang = self.cekKurang()
        x, y = self.findEmptySlot()
        par = (x+y) % 2
        total = kurang + par

        print("Kurang(i) =", kurang)
        print("X =", par)
        print("Total =", total, end="")

        isSolveable = total%2

        if (isSolveable == 0):
            print(" (even)\nSOLVEABLE!")
        else:
            print(" (odd)\nUNSOLVEABLE!")
        
        return isSolveable == 0

    def moveEmpty(self, direction):
        dr = 0
        dc = 0
        if direction == "UP":
            dr = -1
        elif direction == "DOWN":
            dr = 1
        elif direction == "RIGHT":
            dc = 1
        elif direction == "LEFT":
            dc = -1

        row, col = self.findEmptySlot()
        newRow = row+dr
        newCol = col + dc

        if (newRow>=0 and newRow<4 and newCol>=0 and newCol<4):
            #Swap content in row, col w/ newRow, newCol
            nextStateMatrix =  copy.deepcopy(self.arr)
            temp = nextStateMatrix[newRow][newCol]
            nextStateMatrix[newRow][newCol] = 16
            nextStateMatrix[row][col] = temp
            return nextStateMatrix
        else:
            return None





        