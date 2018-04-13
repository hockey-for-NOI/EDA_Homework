from io_utils import load_input, print_result

from asap import pred2succ, asap
from alap import alap

def grid(n, m, optype, rest, pred):
	lb = asap(n, m, optype, rest, pred)
	ub = alap(n, m, optype, rest, pred)
	priority = [j - i for i, j in zip(lb, ub)]

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

		q = sorted(q, key=lambda x:priority[x])

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
	result = grid(n, m, optype, rest, pred)
	print_result(result, outfile)

if __name__ == "__main__":
	main("input.txt", "output_grid.txt")
