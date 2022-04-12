import Vector3n

# class Matrix3n file
class Matrix3n:
	def __init__(self, m0, m3, m6, m1, m4, m7, m2, m5, m8):
		self.matrixData = [m0, m1, m2, m3, m4, m5, m6, m7, m8]

	#print matrix data
	def show(self):
		print("[" + str(self.matrixData[0]) + ", " + str(self.matrixData[3]) + ", " + str(self.matrixData[6]) + ",\n"
				+ str(self.matrixData[1]) + ", " + str(self.matrixData[4]) + ", " + str(self.matrixData[7]) + ",\n"
				+ str(self.matrixData[2]) + ", " + str(self.matrixData[5]) + ", " + str(self.matrixData[8]) + "]")

	#add 2 matrices
	def add(self, matrix):
		mat = Matrix3n(self.matrixData[0] + matrix.matrixData[0], 
					   self.matrixData[1] + matrix.matrixData[1], 
					   self.matrixData[2] + matrix.matrixData[2], 
					   self.matrixData[3] + matrix.matrixData[3], 
					   self.matrixData[4] + matrix.matrixData[4], 
					   self.matrixData[5] + matrix.matrixData[5], 
					   self.matrixData[6] + matrix.matrixData[6], 
					   self.matrixData[7] + matrix.matrixData[7], 
					   self.matrixData[8] + matrix.matrixData[8])

		return mat
	def __add__(self, matrix):
		mat = Matrix3n(self.matrixData[0] + matrix.matrixData[0], 
					   self.matrixData[1] + matrix.matrixData[1], 
					   self.matrixData[2] + matrix.matrixData[2], 
					   self.matrixData[3] + matrix.matrixData[3], 
					   self.matrixData[4] + matrix.matrixData[4], 
					   self.matrixData[5] + matrix.matrixData[5], 
					   self.matrixData[6] + matrix.matrixData[6], 
					   self.matrixData[7] + matrix.matrixData[7], 
					   self.matrixData[8] + matrix.matrixData[8])

		return mat

	#subtract 2 matrices
	def sub(self, matrix):
		mat = Matrix3n(self.matrixData[0] - matrix.matrixData[0], 
					   self.matrixData[1] - matrix.matrixData[1], 
					   self.matrixData[2] - matrix.matrixData[2], 
					   self.matrixData[3] - matrix.matrixData[3], 
					   self.matrixData[4] - matrix.matrixData[4], 
					   self.matrixData[5] - matrix.matrixData[5], 
					   self.matrixData[6] - matrix.matrixData[6], 
					   self.matrixData[7] - matrix.matrixData[7], 
					   self.matrixData[8] - matrix.matrixData[8])

		return mat
	def __sub__(self, matrix):
		mat = Matrix3n(self.matrixData[0] - matrix.matrixData[0], 
					   self.matrixData[1] - matrix.matrixData[1], 
					   self.matrixData[2] - matrix.matrixData[2], 
					   self.matrixData[3] - matrix.matrixData[3], 
					   self.matrixData[4] - matrix.matrixData[4], 
					   self.matrixData[5] - matrix.matrixData[5], 
					   self.matrixData[6] - matrix.matrixData[6], 
					   self.matrixData[7] - matrix.matrixData[7], 
					   self.matrixData[8] - matrix.matrixData[8])

		return mat

	#multiply two matrices
	def multS(self, s):
		mat = Matrix3n(self.matrixData[0] * s, 
					   self.matrixData[1] * s, 
					   self.matrixData[2] * s, 
					   self.matrixData[3] * s, 
					   self.matrixData[4] * s, 
					   self.matrixData[5] * s, 
					   self.matrixData[6] * s, 
					   self.matrixData[7] * s, 
					   self.matrixData[8] * s)

		return mat

	#multiply two matrices
	def mult(self, m):
		mat = Matrix3n(self.matrixData[0] * m.matrixData[0] + self.matrixData[3] * m.matrixData[1] + self.matrixData[6] * m.matrixData[2],
                       self.matrixData[0] * m.matrixData[3] + self.matrixData[3] * m.matrixData[4] + self.matrixData[6] * m.matrixData[5],
                       self.matrixData[0] * m.matrixData[6] + self.matrixData[3] * m.matrixData[7] + self.matrixData[6] * m.matrixData[8],

                       self.matrixData[1] * m.matrixData[0] + self.matrixData[4] * m.matrixData[1] + self.matrixData[7] * m.matrixData[2],
                       self.matrixData[1] * m.matrixData[3] + self.matrixData[4] * m.matrixData[4] + self.matrixData[7] * m.matrixData[5],
                       self.matrixData[1] * m.matrixData[6] + self.matrixData[4] * m.matrixData[7] + self.matrixData[7] * m.matrixData[8],

                       self.matrixData[2] * m.matrixData[0] + self.matrixData[5] * m.matrixData[1] + self.matrixData[8] * m.matrixData[2],
                       self.matrixData[2] * m.matrixData[3] + self.matrixData[5] * m.matrixData[4] + self.matrixData[8] * m.matrixData[5],
                       self.matrixData[2] * m.matrixData[6] + self.matrixData[5] * m.matrixData[7] + self.matrixData[8] * m.matrixData[8])
		return mat
	def __mul__(self, m):
		mat = Matrix3n(self.matrixData[0] * m.matrixData[0] + self.matrixData[3] * m.matrixData[1] + self.matrixData[6] * m.matrixData[2],
                       self.matrixData[0] * m.matrixData[3] + self.matrixData[3] * m.matrixData[4] + self.matrixData[6] * m.matrixData[5],
                       self.matrixData[0] * m.matrixData[6] + self.matrixData[3] * m.matrixData[7] + self.matrixData[6] * m.matrixData[8],

                       self.matrixData[1] * m.matrixData[0] + self.matrixData[4] * m.matrixData[1] + self.matrixData[7] * m.matrixData[2],
                       self.matrixData[1] * m.matrixData[3] + self.matrixData[4] * m.matrixData[4] + self.matrixData[7] * m.matrixData[5],
                       self.matrixData[1] * m.matrixData[6] + self.matrixData[4] * m.matrixData[7] + self.matrixData[7] * m.matrixData[8],

                       self.matrixData[2] * m.matrixData[0] + self.matrixData[5] * m.matrixData[1] + self.matrixData[8] * m.matrixData[2],
                       self.matrixData[2] * m.matrixData[3] + self.matrixData[5] * m.matrixData[4] + self.matrixData[8] * m.matrixData[5],
                       self.matrixData[2] * m.matrixData[6] + self.matrixData[5] * m.matrixData[7] + self.matrixData[8] * m.matrixData[8])
		return mat

	#set matrix as an identity matrix
	def setAsIdentityMatrix(self):
		i = 0
		while(i < 9):
			self.matrixData[i] = 0.0
			i += 1
		self.matrixData[0] = self.matrixData[4] = self.matrixData[8] = 1.0

	#set as inverse matrix
	def setAsInverseMatrix(self, m):
		t1 = m.matrixData[0] * m.matrixData[4]
		t2 = m.matrixData[0] * m.matrixData[7]
		t3 = m.matrixData[3] * m.matrixData[1]
		t4 = m.matrixData[6] * m.matrixData[1]
		t5 = m.matrixData[3] * m.matrixData[2]
		t6 = m.matrixData[6] * m.matrixData[2]

		det = (t1 * m.matrixData[8] - t2 * m.matrixData[5] - t3 * m.matrixData[8] + t4 * m.matrixData[5] + t5 * m.matrixData[7] - t6 * m.matrixData[4])

		if(det == 0.0):return

		invd = 1.0 / det

		m0 = (m.matrixData[4] * m.matrixData[8] - m.matrixData[7] * m.matrixData[5]) * invd		
		m3 = -(m.matrixData[3] * m.matrixData[8] - m.matrixData[6] * m.matrixData[5]) * invd
		m6 = (m.matrixData[3] * m.matrixData[7] - m.matrixData[6] * m.matrixData[4]) * invd
		m1 = -(m.matrixData[1] * m.matrixData[8] - m.matrixData[7] * m.matrixData[2]) * invd
		m4 = (m.matrixData[0] * m.matrixData[8] - t6) * invd
		m7 = -(t2 - t4) * invd
		m2 = (m.matrixData[1] * m.matrixData[5] - m.matrixData[4] * m.matrixData[2]) * invd
		m5 = -(m.matrixData[0] * m.matrixData[5] - t5) * invd
		m8 = (t1 - t3) * invd

		self.matrixData[0] = m0
		self.matrixData[3] = m3
		self.matrixData[6] = m6

		self.matrixData[1] = m1
		self.matrixData[4] = m4
		self.matrixData[7] = m7

		self.matrixData[2] = m2
		self.matrixData[5] = m5
		self.matrixData[8] = m8

	#get inverse of matrix
	def getInverseofMatrix(self):
		matrix = Matrix3n(0, 0, 0, 0, 0, 0, 0, 0, 0)
		matrix.setAsInverseMatrix(self)
		return matrix
	#invert matrix
	def invertMatrix(self):
		self.setAsInverseMatrix(self)

	#set matrix as transposed
	def setMatrixAsTransposed(self, m):
		self.matrixData[0] = m.matrixData[0]
		self.matrixData[3] = m.matrixData[1]
		self.matrixData[6] = m.matrixData[2]

		self.matrixData[1] = m.matrixData[3]
		self.matrixData[4] = m.matrixData[4]
		self.matrixData[7] = m.matrixData[5]

		self.matrixData[2] = m.matrixData[6]
		self.matrixData[5] = m.matrixData[7]
		self.matrixData[8] = m.matrixData[8]
	#get transposed of matrix
	def getTransposed(self):
		matrix = Matrix3n(0, 0, 0, 0, 0, 0, 0, 0, 0)
		matrix.setMatrixAsTransposed(self)
		return matrix

	#vector transformation by 
	def transformVector(self, vect):
		vect = Vector3n(self.matrixData[0] * vect.x + self.matrixData[3] * vect.y + self.matrixData[6] * vect.z,
						self.matrixData[1] * vect.x + self.matrixData[4] * vect.y + self.matrixData[7] * vect.z,
						self.matrixData[2] * vect.x + self.matrixData[5] * vect.y + self.matrixData[8] * vect.z,
						)
		return vect











