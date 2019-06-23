def solution(xs):
	l = filter(lambda x: x != 0, xs)
	if len(xs) < 2: return str(xs[0])
	# Get the negatives and even their number out
	n = filter(lambda x: x < 0, l)
	# Max in the negatives is the minimum in absolute value
	if len(n) % 2 != 0 and len(xs) > 1: l.remove(max(n))
	return str(reduce(lambda x, y: x * y, l) if len(l) > 0 else 0)

if __name__ == "__main__":
	test = [
		[2, 0, 2, 2, 0],
		[-2, -3, 4, -5],
		[-2, 1],
		[-2, -1],
		[-2, -1, 1],
		[-4],
		[1],
		[-2, 0],
		[0],
	]
	for case in test:
		# Solution fails Test 5
		print case, solution(case)