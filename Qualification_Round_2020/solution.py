# time remain = deadline - time(singup) - time(total)

import numpy as np
#import tqdm
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

	B, L, D = list(map(int, lines[0].strip().split())) # books libraries days
	book_scores = list(map(int, lines[1].strip().split()))
	libraries = list()

	for line_ix in range(1, len(lines)//2):

		N, T, M = list(map(int, lines[line_i*2].strip().strip())) #Books, Signup Time, Throughput
		books = set(map(int, lines[line_ix*2 + 1].strip().split())) #taking the id of the books in the perticular library 
		libraries.append(Library(N, T, M, books))


	def get_best_books(library, assigned_books, curr_time):

		time = D - library.singup_time - curr_time  #checking the time availability

		sorted_books = sorted(library.books - assigned_books, key lmabda = b: -book_scores[b])

		return list(sorted_books)[:time*library.n_books_day]


	def score(library, assigned_books, curr_time, assigned_library):
		if library in assigned_library: 
			return float('-inf')

		possible_books = get_best_books(library, assigned_books, curr_time)

		score = sum(book_scores[i] for i in possible_books)

		score = score / library.singup_time

		return score

	#declaring variables and making some new dara set
	assigned_books = set()

	curr_time = 0 

	assigned_libraries = set()

	asm_books = []

	asm_libraries = []

	















