
class Node:
    def __init__(self, node):
        self.value = node
        self.left = None
        self.right = None
        
        
def findLevel(root,record,level):
    print(root.value)
    record[root.value]=level
    if root.left is not None: 
        findLevel(root.left,record,level+1)
    if root.right is not None:
        findLevel(root.right,record,level+1)
    return record
def findParent(root,record,preVal):
    record[root.value]=preVal
    if root.left is not None:
        findParent(root.left,record,root.value)
    if root.right is not None:
        findParent(root.right,record,root.value)
    return record
   
f1=Node(0)
f2=Node(0)
levels=dict()
parents=dict()
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.right = Node(15) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8)

levels=findLevel(root,levels,0)

parents=findParent(root,parents,-1)
x=5
y=8
print(levels)
print(parents)
if levels[x] is levels[y] and parents[x] is not parents[y]:
    print("cousins")
else:
    print("not cousins")

