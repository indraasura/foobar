def answer(m):
	length = len(m)

	matrix = []

	terminal = []
	for i in xrange(len(m)):
		if sum(m[i]) == 0:
			terminal += [ i ]

	matrix = [ m[i] for i in xrange(length) if i not in terminal ]

	if len(matrix) == 0:
		return [1, 1]

	def transposeMatrix(m):
		return map(list,zip(*m))

	def getMatrixMinor(m,i,j):
		return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

	def getMatrixDeternminant(m):
		#base case for 2x2 matrix
		if len(m) == 2:
			return m[0][0]*m[1][1]-m[0][1]*m[1][0]

		determinant = 0
		for c in range(len(m)):
			determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
		return determinant

	def getMatrixInverse(m):
		determinant = getMatrixDeternminant(m)
		#special case for 2x2 matrix:
		if len(m) == 2:
			return [[m[1][1]/determinant, -1*m[0][1]/determinant],
					[-1*m[1][0]/determinant, m[0][0]/determinant]]

		#find matrix of cofactors
		cofactors = []
		for r in range(len(m)):
			cofactorRow = []
			for c in range(len(m)):
				minor = getMatrixMinor(m,r,c)
				cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
			cofactors.append(cofactorRow)
		cofactors = transposeMatrix(cofactors)
		for r in range(len(cofactors)):
			for c in range(len(cofactors)):
				cofactors[r][c] = cofactors[r][c]/determinant
		return cofactors
	
	def createIdentityMatrix(dim):
		mat = []
		for i in xrange(dim):
			k = []
			for j in xrange(dim):
				if i == j:
					k.append(1)
				else:
					k.append(0)
			mat.append(k)
		return mat

	def createMainMatrix(m):
		l = len(m)
		for i in xrange(l):
			for j in xrange(l):
				if i == j:
					m[i][j] = 1 - m[i][j]
				else:
					m[i][j] = 0 - m[i][j]
		return m

	matmul = lambda X, Y: [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

	def lcm(x, y):
		if x > y:
			greater = x
		else:
			greater = y

		while(True):
			if((greater % x == 0) and (greater % y == 0)):
			 	lcm = greater
				break
			greater += 1

		return lcm

	from fractions import Fraction

	for i in xrange(len(m)):
		s = sum(m[i])
		if s != 0:
			m[i] = map(lambda x: Fraction(x, s), m[i])

	terminal.sort()

	P = []
	nonterminal = [ i for i in xrange(length) if i not in terminal ]
	orderP = terminal + nonterminal

	k = len(terminal)

	for r in terminal:
		P.append(m[r])

	for r in nonterminal:
		row = []
		for i in orderP:
			row.append(m[r][i])
		P.append(row)

	Q, R = [], []

	for i in xrange(k, length):
		Q.append(P[i][k:])
		R.append(P[i][:k])

	IQ = createMainMatrix(Q)
	F = getMatrixInverse(IQ)
	FR = matmul(F, R)
	D = FR[0]

	numerator = [ d.numerator for d in D ]
	denominator = [ d.denominator for d in D ]

	LCM = reduce(lambda x, y: lcm(x, y), denominator)

	for i in xrange(len(numerator)):
		numerator[i] *= ( LCM / denominator[i])

	numerator.append(LCM)

	return numerator

if __name__ == "__main__":
	assert (
		answer([
			[0, 2, 1, 0, 0],
			[0, 0, 0, 3, 4],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0]
		]) == [7, 6, 8, 21]
	)
	 
	assert (
		answer([
			[0, 1, 0, 0, 0, 1],
			[4, 0, 0, 3, 2, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]) == [0, 3, 2, 9, 14]
	)
	 
	assert (
		answer([
			[1, 2, 3, 0, 0, 0],
			[4, 5, 6, 0, 0, 0],
			[7, 8, 9, 1, 0, 0],
			[0, 0, 0, 0, 1, 2],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0]
		]) == [1, 2, 3]
	)
	assert (
		answer([
			[0]
		]) == [1, 1]
	)
	 
	assert (
		answer([
			[0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
			[0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
			[0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
			[23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
			[37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [1, 2, 3, 4, 5, 15]
	)
	 
	assert (
		answer([
			[0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
			[0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
			[0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
			[48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
			[0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [4, 5, 5, 4, 2, 20]
	)
	 
	assert (
		answer([
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [1, 1, 1, 1, 1, 5]
	)
	 
	assert (
		answer([
			[1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [2, 1, 1, 1, 1, 6]
	)
	 
	assert (
		answer([
			[0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
			[0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
			[15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [6, 44, 4, 11, 22, 13, 100]
	)
	 
	assert (
		answer([
			[0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
			[0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
			[0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
			[13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
			[0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
			[1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]) == [1, 1, 1, 2, 5]
	)

