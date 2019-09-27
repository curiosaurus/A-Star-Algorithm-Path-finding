class astareg :
#'Common base class for all employees'
    empCount = 0
    g=0
    f=[0,0,0,0,0,0,0,0]
    states={0:'Arad',1:'Timisoura',2:'Pitesti',3:'Zerind',4:'Lugoj',5:'Bucharest',6:'Fagarus',7:'Sibiu'}
    mins=0
    closelist=[]
    openlist=[]

    def isTrue(self,closelistCheck,startnode,l):
        if(closelistCheck[startnode] or closelistCheck[l]):
            return "false"
        else:
            return "true"
    def track_route(self,a,heuristics,startnode,endnode,parent):
        f=[0,0,0,0,0,0,0,0]
        k=len(self.openlist)
        if(k>=0):
            self.closelist.append(startnode) # add startnode to closed list
        for i in range(8):
            if(a[startnode][i]):
                if(i==endnode):
                    self.closelist.append(i)
                    parent= parent+a[startnode][i]
                    print("Total Distance to destination :",parent)
                    # print(self.closelist)
                    print("Path Generated : ")
                    for i in (self.closelist):
                        print(self.states.get(i),)
                    return 0
                f[i]= parent+a[startnode][i]+heuristics[i] #calculate f(n)
            else:
                f[i]=999 #put infinite to the noded having no connection with start node
        mins=f.index(min(f))
        parent= parent+a[startnode][mins]
        for i in range(len(f)):
            if(f[i]<999 and f[mins] != f[i]):
                self.openlist.append(i)
        self.track_route(a,heuristics,mins,endnode,parent)

astar = astareg()
a = [[0,75,118,140,0,0,0,0], 
[75,0,0,50,0,0,0,0]
,[118,0,0,0,0,0,0,0],
[140,50,0,0,0,99,0,80],
[0,0,0,0,0,0,101,97],
[0,0,0,99,0,0,211,0],
[0,0,0,0,101,211,0,0],
[0,0,0,80,97,0,0,0]]
print("Enter Number for Selecting Source and Destination")
print("0:Arad\n1:Timisoura\n2:Pitesti\n3:Zerind\n4:Lugoj\n5:Bucharest\n6:Fagarus\
n7:Sibiu")
startnode=int(input("Enter Starting Point: "))
endnode=int(input("Enter Last Point: "))
parent=0
heuristics=[366,374,329,253,10,176,0,193]
astar.track_route(a,heuristics,startnode,endnode,parent)