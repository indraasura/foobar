def solution(l):
	from itertools import combinations, permutations
	strings = map(str, l)
	universe = []
	for length in xrange(1, len(strings) + 1):
		u = []
		for k in map(list, list(combinations(strings, length))):
			u += list(permutations(k)) 
		universe += sorted(map(lambda l: int(''.join(l)), u), reverse=True)
	needed = filter(lambda e: e % 3 == 0, universe)
	needed.sort(reverse=True)
	return 0 if len(needed) == 0 else needed[0]

if __name__ == "__main__":
	tests = [
		[3, 1, 4, 1],
		[3, 1, 4, 1, 5, 9]
	]
	for case in tests:
		print solution(case)