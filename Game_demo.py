from GAME import maze,COLOR,agent,textLabel
#create maze
m=maze(16,24)
m.CreateMaze(loopPercent=100)

#agent
a=agent(m,footprints=True,color=COLOR.red)
m.enableArrowKey(a)

l1=textLabel(m,'Total Cells',m.rows*m.cols)
l2=textLabel(m,'HINT : Length of Shortest Path', len( m.path)+1 )
m.setupPlayButton({a:m.path})
# m.tracePath({a:m.path},delay=200,kill=True)
m.run()