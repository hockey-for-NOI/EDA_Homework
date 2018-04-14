def intersect(x, y):
    z = [max(x[0], y[0]), max(x[1], y[1]), max(x[2], y[2]),
        min(x[3], y[3]), min(x[4], y[4]), min(x[5], y[5])]
    if z[0] >= z[3] or z[1] >= z[4] or z[2] >= z[5]:
        return None
    return z

def inside(x, y):
    return x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2] and \
        x[3] <= y[3] and x[4] <= y[4] and x[5] <= y[5]

def main(infile, outfile):
    with open(infile, "r") as f:
        data = f.readlines()
    n, m = [int(i) for i in data[0].split()]
    x = [[int(i) for i in j.split()] for j in data[1:n+1]]
    y = [[int(i) for i in j.split()] for j in data[n+1:]]
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

    txt = ["{}\n".format(len(res))]
    for i in res:
        txt.append(" ".join([str(j) for j in i]) + "\n")

    with open(outfile, "w") as f:
        f.writelines(txt)

if __name__ == "__main__":
	main("cube.in", "cube.out")
