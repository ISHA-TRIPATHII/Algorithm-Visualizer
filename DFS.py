from search import maze,robot,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze(2,4)

    dSeacrh,dfsPath,fwdPath=DFS(m,(10,10)) 

    a=robot(m,10,10,goal=(2,4),footprints=True,color=COLOR.blue)
    b=robot(m,2,4,goal=(10,10),footprints=True,color=COLOR.green)
    c=robot(m,10,10,footprints=True,color=COLOR.red,shape='arrow')
    m.tracePath({a:dSeacrh},showMarked=True,delay=120)
    m.tracePath({b:dfsPath},delay=150)
    m.tracePath({c:fwdPath},delay=150)
    l1=textLabel(m,'Algorithm used',"DFS")
    l2=textLabel(m,'Total Cells',m.rows*m.cols)
    l3=textLabel(m,'Length of Shortest Path', len( fwdPath)+1 )
    m.run()

   