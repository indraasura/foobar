def solution(M, F):
	import math
	M, F = float(M), float(F)
	if M % 2 == 0 and F % 2 == 0:
		return "impossible"
	if M == 1 and F == 1:
		return 0

	m, f = M, F
	while True:
		mx, mi = max(M, F), min(M, F)
		gen = math.floor(mx / mi)
		print gen
		break

if __name__ == "__main__":
	cases = [
		('2', '1'),
		('4', '7')
	]
	answers = [
		'1', '4'
	]
	for test, answer in zip(cases, answers):
		print(solution(test[0], test[1]) == answer)