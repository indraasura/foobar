def solution(n):
	steps = 0
	number = int(n)
	while number > 1:
		if number % 2 == 0:
			number /= 2
		elif number == 3 or number % 4 == 1:
			number -= 1
		else:
			number += 1
		steps += 1
	return steps

if __name__ == "__main__":
	print solution(input())