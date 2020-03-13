# time remain = deadline - time(singup) - time(total)

import numpy as np
import tqdm
import os

class Library():
	def __init__ (self, total_n_books, singup_time, n_books_day, books):
		self.total_n_books = total_n_books
		self.singup_time = singup_time
		self.n_books_day = n_books_day
		self.books = books


for FILE in os.listdir('.'):
	if not FILE.endswitch('.txt'):
		continue

	with open(FILE, r) as ifp:
		lines = ifp.readlines()

	B, L, D = list(map(int, lines[0].strip().split()))


