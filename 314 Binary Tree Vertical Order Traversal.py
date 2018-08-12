# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        my=[0,0]
        mydict={}
        
        def travel(root,val,depth):
            
            if root:
                if mydict.has_key(val):
                    temp=mydict.get(val)
                else:
                    mydict[val]=[]
                
                t=[]
                
                t.append(root.val)
                t.append(depth)
                mydict.get(val).append(t)
                #print mydict
                my[0]=min(my[0],val)
                my[1]=max(my[1],val)
                travel(root.left,val-1,depth+1)
                travel(root.right,val+1,depth+1)
        
        
        travel(root,0,0)
        
        result=[]
        for i in range(my[0],my[1]+1):
            temp=mydict.get(i)
            #print temp
            temp.sort(lambda x,y:cmp(x[1],y[1])) 
            #print temp
            #temp.sort(lambda x+y:cmp(x[0],y[0]))
            mysave=[]
            for j in temp:
                mysave.append(j[0])
            result.append(mysave)
        return result
        
        