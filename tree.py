import collections

 
class Tree(object):
    # -----------------------------------------------------Tree object init
    def __init__(self, data = None, children = None):
        # object = Tree("optional name", [optional list of children])
        self.data = data
        self.__children = []
        self.__parent=None
        
        if children:
            # add child if one Tree object
            if isinstance(children, Tree):
                self.__children.append(children)
                children.__parent = self 
            
            # add children if iterable
            elif isinstance(children, collections.Iterable):
                for child in children:
                    # checking object type
                    if isinstance(child, Tree):
                        self.__children.append(child)
                        child.__parent = self
                    else:
                        raise TypeError('Child of Tree should be a Tree type.')      
            else:
                raise TypeError('Child of Tree should be a Tree type')
    
    # -----------------------------------------------------security & str conversion
    def __setattr__(self, name, value):
        if name in ('parent', '__parent', 'children'):
                raise AttributeError("To add children, please use addChild or addChildren method.")
        else:
            super().__setattr__(name, value)
            
    def __str__(self, *args, **kwargs):
        return self.data.__str__(*args, **kwargs)

    # -----------------------------------------------------adding child/ren
    def addChild(self, child):
        if isinstance(child, Tree):
                self.__children.append(child)
                child.__parent = self
        else:
                raise TypeError('Child of Tree should be a Tree type')
            
    def addChildren(self, children):
        if isinstance(children, list):
                for child in children:
                    if isinstance(child, Tree):
                        self.__children.append(child)
                        child.__parent = self
                    else:
                        raise TypeError('Child of Tree should be a Tree type.')      
         
    # -----------------------------------------------------getters
    def getParent(self):
        return self.__parent
            
    def getChildren(self):
        # return all children
        return self.__children
        
    def getRoot(self):
        if self.isRoot():
            return self
        else:
            return self.getParent().getRoot()
    
    def getNode(self, content, includeself = True):
        # return first object matching data with content
        nodesQ = []
        
        if includeself:
            nodesQ.append(self)
        else:
            nodesQ.extend(self.getChildren())
            
        while nodesQ:
            child = nodesQ[0]
            if child.data == content:
                return child
            else:
                nodesQ.extend(child.getChildren())
                del nodesQ[0]         

    # -----------------------------------------------------bools
    def nodeExists(self, content, includeself = True):
        if self.getNode(content, includeself) != None:
            return True
        else:
            return False

    def isRoot(self):
        # return true if there are no parents in node
        if self.__parent is None:
            return True
        else:
            return False
      
    # -----------------------------------------------------printers
    def printTree(self):
        # printing the tree in an elegant way

        level = 0
        # init Nodes Stack
        NodesS = [self, level]
        
        while NodesS:
            # head pointer points to the first item of stack, can be a level identifier or tree node 
            head = NodesS.pop()
            if isinstance(head, int):
                level = head
            else:
                self.__printLabel__(head, NodesS, level)
                children = head.getChildren()
                children.reverse()
                
                if NodesS:
                    # push level info if stack is not empty
                    NodesS.append(level)
                
                if children:
                    # add children if has children nodes 
                    NodesS.extend(children)
                    level += 1
                    NodesS.append(level)
          
    def __printLabel__(self, head, NodesS, level):
        # function used to print single node
        leading = '' 
        lasting = ' |___ '
        label = str(head.data)
        
        if level == 0:
            print(str(head))
        else:
            for l in range(0, level - 1):
                sibling = False
                parentT = head.__getParent__(level - l)
                for c in parentT.getChildren():
                    if c in NodesS:
                        sibling = True
                        break
                if sibling:
                    leading += ' |   '
                else:
                    leading += '      '
            
            if label.strip() != '': 
                print('{0}{1}{2}'.format( leading, lasting, label))
        
    def __getParent__(self, up):
        # getter with indicator of depth
        parent = self;
        while up:
            parent = parent.getParent()
            up -= 1
        return parent

            
'''
if __name__ == "__main__":

    root = Tree('Root')
    child1 = Tree('1')
    child2 = Tree('2')
    child3 = Tree('3')
    child11 = Tree('11')
    child31 = Tree('31')
    child111 = Tree('111')

    root.addChildren([child1, child2, child3])
    child1.addChild(child11)
    child3.addChild(child31)
    child11.addChild(child111)
    
    root2 = Tree('Root2')
    childr2 = Tree('r2')
    root2.addChild(childr2)


    root.printTree()
    root2.printTree()

    content = '2'
    if root.nodeExists(content):
        root.getNode(content).addChild(root2)
        print("\n---merging on "+content+"---")
        root.printTree()
'''
