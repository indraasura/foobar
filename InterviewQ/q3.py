import sys

def solution(N, K):
	arrays = []
	
	for i in xrange(0, len(N) - K + 1):
		arrays.append(N[i:i+K])
	
	def getGreaterArray(x, y):
		for i in xrange(len(x)):
			if x[i] > y[i]:
				return x
			elif x[i] < y[i]:
				return y
		return x

	return reduce(lambda x, y: getGreaterArray(x,y), arrays)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  N = [int(x) for x in input[0].split(",")]
  K = int(input[1])
  sys.stdout.write(",".join([str(i) for i in solution(N, K)]))


if __name__ == "__main__":
  main()