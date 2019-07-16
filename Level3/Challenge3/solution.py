def solution(M, F):
	M, F = long(M), long(F)
	generation = 0
	while (M != 1 or F != 1) :
		if F <= 0 or M <= 0:
			generation = "impossible"
			break
		if M != 0 and F == 1:
			generation += (M - 1)
			break
		else:
			generation += long(M / F)
			M, F = F, M % F		
	return str(generation)

if __name__ == "__main__":
	cases = [
		('2', '1'),
		('4', '7')
	]
	answers = [
		1, 4
	]
	for test, answer in zip(cases, answers):
		print(solution(test[0], test[1]))