src = [[c for c in input()] for _ in range(8)]
# for i in range(2,6):
#     for j in range(2,6):
#         if src[i][j] == "." and src[i-2][j] == "." and src[i+2][j] == "." and src[i][j-2] == "." and src[i][j+2] == ".":
#             src[i][j] = "C"
# for i in range(8):
#     print(src[i])

def search(x,y,f,ti):
    cur = src[x][y]
    # print(x,y,cur,ti)
    if cur == "D":
        return ti+"D"
    elif cur == "I":
        src[x][y] = "."
        return search(x,y,f,ti[:-1]+"X"+ti[-1])
    elif cur == "C":
        return ti+"C"
    elif cur in ".T":
        subcmd = []
        src[x][y] = "C"
        if f==0:
            if not y == 7:
                subcmd.append(search(x,y+1,0,"F"))
                # # src[x][y] = "."
            if not x == 0:
                # src[x][y] = "C"
                subcmd.append(search(x-1,y,1,"LF"))
                # # src[x][y] = "."
            if not x == 7:
                # src[x][y] = "C"
                subcmd.append(search(x+1,y,3,"RF"))
                # # src[x][y] = "."
            # src[x][y] = "."
        elif f==2:
            if not y == 0:
                # src[x][y] = "C"
                subcmd.append(search(x,y-1,2,"F"))
                # # src[x][y] = "."
            if not x == 0:
                # src[x][y] = "C"
                subcmd.append(search(x-1,y,1,"RF"))
                # # src[x][y] = "."
            if not x == 7:
                # src[x][y] = "C"
                subcmd.append(search(x+1,y,3,"LF"))
                # # src[x][y] = "."
            # src[x][y] = "."
        elif f==1:
            if not x == 0:
                # src[x][y] = "C"
                subcmd.append(search(x-1,y,1,"F"))
                # # src[x][y] = "."
            if not y == 0:
                # src[x][y] = "C"
                subcmd.append(search(x,y-1,2,"LF"))
                # # src[x][y] = "."
            if not y == 7:
                # src[x][y] = "C"
                subcmd.append(search(x,y+1,0,"RF"))
                # # src[x][y] = "."
            # src[x][y] = "."
        elif f==3:
            if not x == 7:
                # src[x][y] = "C"
                subcmd.append(search(x+1,y,3,"F"))
                # # src[x][y] = "."
            if not y == 0:
                # src[x][y] = "C"
                subcmd.append(search(x,y-1,2,"RF"))
                # # src[x][y] = "."
            if not y == 7:
                # src[x][y] = "C"
                subcmd.append(search(x,y+1,0,"LF"))
                # # src[x][y] = "."
            # src[x][y] = "."
        src[x][y] = "."
        avaCmd = []
        for c in subcmd:
            if c[-1] == "D":
                avaCmd.append(c)
        if avaCmd:
            shortI = 0
            for i in range(len(avaCmd)):
                if len(avaCmd[shortI]) > len(avaCmd[i]):
                    shortI = i
            return ti + avaCmd[shortI]
        else:
            return ti + " "

cmd = search(7,0,0,"").replace(" ", "")
if cmd == "":
    print("no solution")
else:
    print(cmd[:-1])
