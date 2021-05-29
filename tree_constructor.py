from tree import Tree
import sys

file_locations = ["examples\example1.cpp", "examples\example2.cpp"]


def getNodeTree(cname):
    for x in trees:
        node = x.getNode(cname)
        if node != None:
            return node

def addClass(cname):
    if getNodeTree(cname) == None:
        trees.append(Tree(cname))

def addParent(cname, pname):
    pnode = getNodeTree(pname)
    if pnode != None:
        cnode = getNodeTree(cname)
        if cnode != None:
            pnode.addChild(cnode)
            trees.remove(cnode)
        else:
            pnode.addChild(Tree(cname))


if __name__ == "__main__":

    # user arguments
    if len(sys.argv) == 1:
        pass
    else:
        file_locations = sys.argv[1:]

    if file_locations == []:
        print("No file provided.")

        
    for location in file_locations:
        try:
            trees = []
            print("File: " + str(location))
            f = open(location)

            comment = False
            for line in f:
                linia = line.split()
                    
                for i in range(len(linia)):
                    # ignoring possible comments
                    if "//" in linia[i]:
                        break
                    elif "/*" in linia[i]:
                        comment = True
                    elif "*/" in linia[i]:
                        comment = False
                    elif comment:
                        pass

                    # class occured
                    elif linia[i] == "class":
                        klasa = linia[i+1].replace(";","").replace("{","")
                        addClass(klasa)

                    # parenting occured
                    elif linia[i] == ":" and linia[i-2] == "class":
                        for j in range(1,4):
                            if linia[i+j] in ["private", "public", "protected", "virtual"]:
                                pass
                            else:
                                klasa = linia[i+j].replace(";","").replace("{","")
                                addParent(linia[i-1], klasa)
                                break
            f.close()
            for tree in trees:
                tree.printTree()
                print("")
            print("")
        except IOError:
            # error if there are any problems with the file
            print("-File not accessible\n")
            

    
