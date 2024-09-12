from search import maze,robot,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)

    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath
if __name__=='__main__':

    m=maze(20,20)
    m.CreateMaze(loopPercent=100,theme='dark')
    bSearch,bfsPath,fwdPath=BFS(m)
    a=robot(m,footprints=True,color=COLOR.blue,shape='square',filled=False)
    b=robot(m,footprints=True,color=COLOR.green,shape='arrow',filled=True)
    c=robot(m,1,1,footprints=True,color=COLOR.red,shape='square',goal=(m.rows,m.cols))
    m.tracePath({a:bSearch},delay=120)
    m.tracePath({c:bfsPath},delay=150)
    m.tracePath({b:fwdPath},delay=150)
    l1=textLabel(m,'Algorithm used',"BFS")
    l2=textLabel(m,'Total Cells',m.rows*m.cols)
    l3=textLabel(m,'Length of Shortest Path', len( fwdPath)+1 )

    m.run()