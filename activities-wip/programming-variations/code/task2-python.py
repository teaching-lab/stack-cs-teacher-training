class createnode:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

class createbinarysearchtree:
    def __init__(self, data = None):
        self.top=None   

    def RecursBST(self,top,data):            
        if self.top is None:
            self.top=createnode(data)                
        elif  self.top.root>data:
            self.top.left=self.RecursBST(self.top.left,data)
        elif  self.top.root<data:
            self.top.right=self.RecursBST(self.top.right,data)

# Problematic inputs
conv=createbinarysearchtree();
conv.RecursBST(conv.top,50)
conv.RecursBST(conv.top,40)
