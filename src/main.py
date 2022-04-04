import time
from tree import Tree
from priorqueue import PriorityQueue
from matrix import Matrix

# minta input testcase yang ingin dicoba kepada pengguna
doc = input("Enter File to Test: ")
print()

#periksa apakah puzzle sudah solved
def isCompleted(board):
    flatboard = board.toOneDim()

    for i in range(len(flatboard)):
        #solved jika elemen sudah terurut dari 1 sampai 16
        if flatboard[i]-1 != i:
            return False
    return True

directions = ["UP", "RIGHT", "DOWN", "LEFT"]

#inisialisasi board puzzle awal sebagai root node
root = Matrix(doc)

try:
    a = root.arr[0][1]
except:
    print("File not Exists!")
    exit()

root.printMatrix()

if not root.cekSolvabilitas():
    exit()

#inisialisasi priorityqueue
pq = PriorityQueue()
#inisialisasi state space tree
tree = Tree(root)

#masukkan root node ke tree
pq.push(tree)

#variable penyimpan node yang merupakan solusi
sol_node = None

completed = False
node_counter = 1
starttime = time.process_time_ns()


#main branch and bound algorithm
while not pq.isEmpty() and not completed:
    node = pq.delete()

    if (isCompleted(node.matrix)):
        sol_node = node 
        completed = True
    
    else:
        for i,direction in enumerate(directions):
            #buat node anak yang arah pergerakannya bukan berlawanna dengan arah gerak node
            if (directions[(i+2)%4] != node.move):
                moved_puzzle = Matrix(node.matrix.moveEmpty(direction))
                #print(direction)
                #jika puzzle dapat digerakkan
                if (moved_puzzle != None and moved_puzzle.arr != None):
                #moved_puzzle.printMatrix()
                    goalCost = moved_puzzle.calculateCost()

                    child = Tree(moved_puzzle, node, node.depth+1, goalCost, direction)
                    #print("hello\n")
                    node_counter +=1
                    pq.push(child)



#telusuri pohon untuk mendapat langkah puzzle
startNode = sol_node
sol_array = []
print()
while (startNode != tree):
    sol_array.insert(0, startNode)
    startNode = startNode.parent

endtime = time.process_time_ns()


#output hasil
# print(len(sol_array))
move_monitor = ""
for i in range(len(sol_array)):
    print("STEP " + str(i+1) + ": " + sol_array[i].move)
    sol_array[i].matrix.printMatrix()
    move_monitor += sol_array[i].move[0] + " "
    print()

print("MOVES:", move_monitor)
print("Node generated:", node_counter)
print("time taken:", end="")
print(((endtime-starttime)/1000000), "ms") 

    




    

