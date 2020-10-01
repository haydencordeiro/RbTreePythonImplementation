

class Node:
    value = None  # value of Node
    color = None  # Red or Black
    left = None  # left child of type node
    right = None  # Right child of type node
    parent = None

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def Setleft(self, node):
        self.left = node

    def Setright(self, node):
        self.right = node


class RBTree:
    root = None

    def __init__(self, value):
        self.root = Node(value, "black")

    def ReColor(self, node):
        if node.color == "black":
            node.color = "red"
        else:
            node.color = "black"

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print(' ' * 6 * level + '|->', str(node.value) +
                  " ({})".format(node.color[0]))
            self.printTree(node.left, level + 1)

    # def getUncle(self, node):
    #     tempNode = self.root
    #     parent = None
    #     gparent = None
    #     while True:
    #         try:
    #             if tempNode.left == None and tempNode.right == None or tempNode.value == node.value:
    #                 break
    #         except:
    #             break
    #         if node.value > tempNode.value and tempNode.right != None:
    #             gparent = parent
    #             parent = tempNode
    #             tempNode = tempNode.right
    #         elif node.value < tempNode.value and tempNode.left != None:
    #             gparent = parent
    #             parent = tempNode
    #             tempNode = tempNode.left

    #     try:
    #         if gparent.left == parent:
    #             return(gparent.right, parent, gparent)
    #         else:
    #             return(gparent.left, parent, gparent)
    #     except:
    #         return None

    # def GetParent(self, node):
    #     tempNode = self.root
    #     parent = None
    #     gparent = None
    #     while True:
    #         try:
    #             if tempNode.left == None and tempNode.right == None or tempNode.value == node.value:
    #                 break
    #         except:
    #             break
    #         if node.value > tempNode.value and tempNode.right != None:
    #             gparent = parent
    #             parent = tempNode
    #             tempNode = tempNode.right
    #         elif node.value < tempNode.value and tempNode.left != None:
    #             gparent = parent
    #             parent = tempNode
    #             tempNode = tempNode.left
    #     return parent

    # def RightRotate(self, x):
    #     y = x.left
    #     x.left = x.right
    #     y.right.parent=x
    #     y.parent=x.parent
    #     if y.right != None:
    #         tempN = self.GetParent(y.right)
    #         tempN = x
    #     xparent, yparent = self.GetParent(x), self.GetParent(y)
    #     yparent = xparent
    #     xparent, yparent = self.GetParent(x), self.GetParent(y)
    #     if xparent == None:
    #         self.root = y
    #         xparent, yparent = self.GetParent(x), self.GetParent(y)

    #     elif x == xparent.left:
    #         xparent.left = y
    #     else:
    #         xparent.right = y
    #     y.right = x
    #     xparent = y

    def InsertNode(self, value):
        insNode = None
        tempNode = self.root
        while True:
            if(value > tempNode.value and tempNode.right == None):
                insNode = Node(value, "red")
                tempNode.right = insNode
                insNode.parent = tempNode

                break
            elif(value < tempNode.value and tempNode.left == None):
                insNode = Node(value, "red")
                tempNode.left = insNode
                insNode.parent = tempNode

                break
            elif(value > tempNode.value):
                tempNode = tempNode.right
            else:
                tempNode = tempNode.left
        self.InsertFixUp(insNode)

        return insNode

    # def InsertFixUp(self, z):
    #     try:
    #         while z.parent.color == "red":

    #             if z.parent == z.parent.parent.left:
    #                 y = z.parent.parent.right
    #                 if y.color == "red":
    #                     z.parent.color = "black"
    #                     y.color = "black"
    #                     z.parent.parent.color = "red"
    #                     z = z.parent.parent
    #                 elif z == z.parent.right:
    #                     z = z.parent
    #                     self.LeftRotate(z)
    #                 z.parent.color = "black"
    #                 z.parent.parent.color = "red"
    #                 self.RightRotate(z.parent.parent)

    #             if z.parent == z.parent.parent.right:
    #                 y = z.parent.parent.left
    #                 if y.color == "red":
    #                     z.parent.color = "black"
    #                     y.color = "black"
    #                     z.parent.parent.color = "red"
    #                     z = z.parent.parent
    #                 elif z == z.parent.left:
    #                     z = z.parent
    #                     self.RightRotate(z)
    #                     z.parent.color = "black"
    #                     z.parent.parent.color = "red"
    #                     self.LeftRotate(z.parent.parent)

    #     except:
    #         pass
    #         self.root.color = "black"
    def getUncle(self, node):
        try:
            if node.parent.parent.left == node.parent:
                return node.parent.parent.right
            else:
                return node.parent.parent.left
        except:
            return Node(-1, "black")

    def InsertFixUp(self, node):

        if self.root.color == "red":
            self.root.color = "black"
        uncle = self.getUncle(node)
        try:
            if uncle.color == "red":
                ReColor(uncle)
                ReColor(node.parent)
                ReColor(node.parent.parent)
            if uncle.color == "black":
                if node.parent.right == node and node.parent.parent.right == node.parent:  # case 4
                    ReColor(uncle)
                    ReColor(node.parent)
                    LeftRotate(node.parent.parent)
                elif node.parent.left == node and node.parent.parent.left == node.parent:  # case 4
                    ReColor(uncle)
                    ReColor(node.parent)
                    RightRotate(node.parent.parent)
                if node.parent.right == node and node.parent.parent.right != node.parent:  # case 3
                    LeftRotate(node.parent)
                elif node.parent.left != node and node.parent.parent.left != node.parent:  # case 3
                    RightRotate(node.parent)
        except:
            pass
    # def RightRotate(self, x):
    #     y = x.left
    #     x.left = y.right
    #     y.right.parent = x
    #     y.parent = x.parent
    #     if x.parent == None:
    #         self.root = y
    #     elif x == x.parent.right:
    #         x.parent.right = y
    #     else:
    #         x.parent.left = y
    #     y.right = x
    #     x.parent = y

    def LeftRotate(self, x):
        try:
            y = x.right
            x.right = y.left
            if y.left != None:
                y.left.parent = x
            y.parent = x.parent
            if x.parent == None:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
            y.left = x
            x.parent = y
        except:
            pass

    def RightRotate(self, x):
        try:
            y = x.left
            x.left = y.right
            if y.right != None:
                y.right.parent = x
            y.parent = x.parent
            if x.parent == None:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
            y.right = x
            x.parent = y
        except:
            pass


# tree = RBTree(10)
# g = tree.InsertNode(5, )
# s = tree.InsertNode(12)
# x = tree.InsertNode(16)
# d = tree.InsertNode(11)
# a = tree.InsertNode(18)
# tree.InsertNode(15)
# tree.printTree(tree.root)
# tree.RightRotate(tree.root)

# print()
# print()
# print()
# print()
# tree.printTree(tree.root)


# tree = RBTree(10)
# tree.InsertNode(90)
# tree.InsertNode(5)
# tree.InsertNode(20)
# tree.InsertNode(6)
# tree.InsertNode(9)
# tree.printTree(tree.root)
tree = RBTree(41)
tree.printTree(tree.root)
print()
tree.InsertNode(38)
tree.printTree(tree.root)
print()
tree.InsertNode(31)
tree.printTree(tree.root)
print()
tree.InsertNode(12)
tree.printTree(tree.root)
print()
tree.InsertNode(19)
tree.printTree(tree.root)
print()
tree.InsertNode(8)
tree.printTree(tree.root)
print()
