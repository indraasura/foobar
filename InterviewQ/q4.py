import sys

def solution(A, B):
  """Your solution goes here."""
  stringsA = A.split(',')
  stringsB = B.split(',')

  def isSmallerString(a, b):
  	smallestA = sorted(a)[0]
  	smallestB = sorted(b)[0]
  	return a.count(smallestA) < b.count(smallestB)

  c = []

  for b in stringsB:
	d = 0
  	for a in stringsA:
  		if isSmallerString(a, b):
  			d += 1
	c.append(d)

  return c


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = input[0]
  B = input[1]
  sys.stdout.write(",".join([str(i) for i in solution(A, B)]))


if __name__ == "__main__":
  main()
