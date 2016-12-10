src = [[c for c in input()] for _ in range(8)]
cmd = input()
loc = [7,0]
f = 0
try:
    for c in cmd:
        if c == 'F':
            if f == 0:
                loc[1] += 1
            elif f == 1:
                loc[0] -= 1
            elif f == 2:
                loc[1] -= 1
            elif f == 3:
                loc[0] += 1
            if not src[loc[0]][loc[1]] in ".D" :
                raise
        elif c == 'L':
            f += 1
            f = f % 4
        elif c == "R":
            f -= 1
            f = f % 4
        elif c == "X":
            if f == 0:
                if src[loc[0]][loc[1]+1] != "I":
                    raise
                else:
                    src[loc[0]][loc[1]+1] = "."
            if f == 1:
                if src[loc[0]-1][loc[1]] != "I":
                    raise
                else:
                    src[loc[0]-1][loc[1]] = "."
            if f == 2:
                if src[loc[0]][loc[1]-1] != "I":
                    raise
                else:
                    src[loc[0]][loc[1]-1] = "."
            elif f == 3:
                if src[loc[0]+1][loc[1]] != "I":
                    raise
                else:
                    src[loc[0]+1][loc[1]] = "."
    if src[loc[0]][loc[1]] == "D":
        print("Diamond!")
    else:
        raise
except:
    print("Bug!")
