def intersect(x, y):
    z = []
    for i, j in zip(x, y):
        if i == 'X':
            z.append(j)
        elif j == 'X':
            z.append(i)
        elif i == j:
            z.append(i)
        else:
            return None

    return "".join(z)

def inside(x, y):
    for i, j in zip(x, y):
        if i != j and j != 'X':
            return False

    return True

def main(infile, outfile):
    with open(infile, "r") as f:
        data = f.readlines()

    n, m, k = [int(i) for i in data[0].split()]

    x = data[1:n+1]
    y = data[n+1:]
    z = []

    for i in x:
        for j in y:
            tmp = intersect(i, j)
            if not tmp is None:
                z.append(tmp)

    res = []
    for id0, i in enumerate(z):
        flag = True
        for id1, j in enumerate(z):
            if id0 != id1 and inside(i, j):
                flag = False
                break
        if flag:
            res.append(i)

    with open(outfile, "w") as f:
        f.writelines(["{}\n".format(len(res))] + res)

if __name__ == "__main__":
    main("logic.in", "logic_intersect.out")
