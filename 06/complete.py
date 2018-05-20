import os
import sys

def main(infile, outfile):
	
	with open(infile, "r") as f:
		data = [[int(j) for j in i.strip().split()] for i in f.readlines()]

	n, m = data[0]
	next_state = data[1:n+1]
	output = enumerate(data[n+1:])
	
	sorted_output = sorted(output, key = lambda x: x[1])
	
	k = 0
	result = [0] * n
	prev = None
	for pid, pv in sorted_output:
		if prev != pv: k += 1
		result[pid] = k - 1
		prev = pv
	
	lastk = n
	while k != lastk:
		lastk = k
		stats = [list() for i in range(k)]
		for pid, pv in enumerate(next_state):
			qv = [result[i] for i in pv]
			stats[result[pid]].append((pid, qv))
		k = 0
		for i in range(lastk):
			prev = None
			for pid, pv in sorted(stats[i], key = lambda x: x[1]):
				if prev != pv: k += 1
				result[pid] = k - 1
				prev = pv
	
	result = "{}\n".format(k) + " ".join([str(i) for i in result])
	with open(outfile, "w") as f:
		f.write(result)


if __name__ == "__main__":
	main("complete.in", "complete.out")
