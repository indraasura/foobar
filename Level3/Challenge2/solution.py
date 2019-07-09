def solution(m):
	terminal = []
	for i in xrange(len(m)):
		state = m[i]
		if all([ x == 0 for x in state ]):
			terminal += [ i ]
	terminal.append("denominator")
	return terminal

if __name__ == "__main__":
	"""
		--- Case 0 ---
		s0 -> s1 -> s3
		s0 -> s1 -> s4
		s0 -> s2
	"""
	cases = [
		[
			[0, 2, 1, 0, 0], # s0
			[0, 0, 0, 3, 4], # s1
			[0, 0, 0, 0, 0], # s2 - Terminal
			[0, 0, 0, 0, 0], # s3 - Terminal
			[0, 0, 0, 0, 0]  # s4 - Terminal
		],
		#
		#	--- Case 1 ---
		#
		[
			[0, 1, 0, 0, 0, 1],
			[4, 0, 0, 3, 2, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]
	]
	answers = [
		[7, 6, 8, 21],
		[0, 3, 2, 9, 14]
	]
	for test, answer  in zip(cases, answers):
		print ""
		print "OUTPUT:\t\t", solution(test)
		print "EXPECTED:\t", answer
		print ""