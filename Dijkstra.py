from Pathfinder import maze,robot,COLOR,textLabel
def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
            



if __name__=='__main__':
    m=maze(16,16)
    m.CreateMaze(1,4,loopPercent=10)
    

    h1=robot(m,4,1,color=COLOR.yellow)
    h2=robot(m,4,2,color=COLOR.red)
    h3=robot(m,4,3,color=COLOR.yellow)
    h4=robot(m,4,4,color=COLOR.red)
    h5=robot(m,4,5,color=COLOR.yellow)
    h6=robot(m,4,6,color=COLOR.red)
    h7=robot(m,4,7,color=COLOR.yellow)
    h8=robot(m,4,8,color=COLOR.red)
    h9=robot(m,8,5,color=COLOR.yellow)
    h10=robot(m,8,6,color=COLOR.red)
    h11=robot(m,8,7,color=COLOR.yellow)
    h12=robot(m,8,8,color=COLOR.red)
    h13=robot(m,8,9,color=COLOR.yellow)
    h14=robot(m,8,10,color=COLOR.red)
    h15=robot(m,8,11,color=COLOR.yellow)
    h16=robot(m,8,12,color=COLOR.red)
    h17=robot(m,12,9,color=COLOR.yellow)
    h18=robot(m,12,10,color=COLOR.red)
    h19=robot(m,12,11,color=COLOR.yellow)
    h20=robot(m,12,12,color=COLOR.red)
    h21=robot(m,12,13,color=COLOR.yellow)
    h22=robot(m,12,14,color=COLOR.red)
    h23=robot(m,12,15,color=COLOR.yellow)
    h24=robot(m,12,16,color=COLOR.red)


    h1.cost=50
    h2.cost=100
    h3.cost=50
    h4.cost=100
    h5.cost=50
    h6.cost=100
    h7.cost=50
    h8.cost=100
    h9.cost=50
    h10.cost=100
    h11.cost=50
    h12.cost=100
    h13.cost=50
    h14.cost=100
    h15.cost=50
    h16.cost=100
    h17.cost=50
    h18.cost=100
    h19.cost=50
    h20.cost=100
    h21.cost=50
    h22.cost=100
    h23.cost=50
    h24.cost=100
   
    path,c=dijkstra(m,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24)
    l1=textLabel(m,'Algorithm used',"Dijkstra")
    l2=textLabel(m,'Total Cells',m.rows*m.cols)
    l3=textLabel(m,'Length of Shortest Path', len(path)+1 )
    textLabel(m,'Total Cost',c)

    # a=robot(m,color=COLOR.cyan,filled=True,footprints=True)
    a=robot(m,color=COLOR.red,filled=True,footprints=True,shape='arrow')
    m.enableArrowKey(a)
    m.setupPlayButton({a:path})
    #m.tracePath({a:path})


    m.run()