def load_input(filename):
	with open(filename, "r") as f:
		data = f.readlines()
	n, m = [int(i) for i in data[0].split()]
	optype = [int(i) - 1 for i in data[1].split()]
	rest = [int(i) for i in data[2].split()]
	pred = [[int(i) - 1 for i in tmp.split()[:-1]] for tmp in data[3:]]
	return n, m, optype, rest, pred

def print_result(result, filename):
	n = max(result) + 1
	trans = [[] for i in range(n + 1)]
	trans[0].append(str(n))
	for idx, pos in enumerate(result):
		trans[pos + 1].append(str(idx + 1))
	tmp = [" ".join(i) + "\n" for i in trans]
	with open(filename, "w") as f:
		f.writelines(tmp)
