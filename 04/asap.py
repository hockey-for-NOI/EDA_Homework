from io_utils import load_input, print_result

def pred2succ(pred):
	succ = [[] for i in pred]
	for i, tmp in enumerate(pred):
		for j in tmp:
			succ[j].append(i)
	return succ

def asap(n, m, optype, rest, pred):
	result = [None] * n
	cur = 0
	succ = pred2succ(pred)

	count = [len(i) for i in pred]

	q = []
	for i in range(n):
		if count[i] == 0:
			q.append(i)

	while len(q) > 0:
		cur_use = [0] * m
		quse = []
		qdelay = []
		for idx in q:
			opt = optype[idx]
			if cur_use[opt] < rest[opt]:
				cur_use[opt] += 1
				result[idx] = cur
				quse.append(idx)
			else:
				qdelay.append(idx)
		q = qdelay
		for idx in quse:
			for tar in succ[idx]:
				count[tar] -= 1
				if count[tar] == 0:
					q.append(tar)
		
		cur += 1
		
	return result

def main(infile, outfile):
	n, m, optype, rest, pred = load_input(infile)
	result = asap(n, m, optype, rest, pred)
	print_result(result, outfile)

if __name__ == "__main__":
	main("input.txt", "output_asap.txt")
