from BFS import BFS
from DFS import DFS
from search import maze,robot,COLOR,textLabel
from timeit import timeit

m=maze(10,10)
# m.CreateMaze(loopPercent=100)
m.CreateMaze(1,1,loopPercent=50)
# m.CreateMaze()
# m.CreateMaze(1,30)
searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)

textLabel(m,'DFS Path Length',len(fwdDFSPath)+1)
textLabel(m,'BFS Path Length',len(fwdBFSPath)+1)
textLabel(m,'DFS Search Length',len(searchPath)+1)
textLabel(m,'BFS Search Length',len(bSearch)+1)

a=robot(m,footprints=True,color=COLOR.cyan)
b=robot(m,footprints=True,color=COLOR.yellow)
m.tracePath({a:fwdBFSPath},delay=100)
m.tracePath({b:fwdDFSPath},delay=100)


t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='BFS(m)',number=1000,globals=globals())

textLabel(m,'DFS Time',t1)
textLabel(m,'BFS Time',t2)


m.run()