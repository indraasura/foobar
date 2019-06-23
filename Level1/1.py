for _ in xrange(input()):
	s = raw_input()
	def solution(s):
		index = (s+s).find(s, 1)
		if index == -1: return 0
		else:
			string = s[:index]
			return s.count(string)
	print solution(s)