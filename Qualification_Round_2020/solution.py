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

	B, L, D = list(map(int, lines[0].strip().split())) # books libraries days
	book_scores = list(map(int, lines[1].strip().split()))
	libraries = list()

	for line_ix in range(1, len(lines)//2):

		N, T, M = list(map(int, lines[line_i*2].strip().strip())) #Books, Signup Time, Throughput
		books = set(map(int, lines[line_ix*2 + 1].strip().split())) #taking the id of the books in the perticular library 
		libraries.append(Library(N, T, M, books))


	def get_best_books(library, assigned_books, curr_time):

		time = D - library.singup_time - curr_time  #checking the time availability

		#sorted_books = sorted(library.books - assigned_books, key lmabda = b: -book_scores[b])
		sorted_books = sorted(library.books - assigned_books, 
				      key=lambda b: -book_scores[b])

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


	# Iteratively take the best possible library and schedule it
	for _ in tqdm(range(L)):
		scores = [score(x, assigned_books, curr_time, assigned_libraries)
			  for x in libraries]

		best_library = np.argmax(libraries[best_library])

		best_books = get_best_books(libraries[best_library], assigned_books, curr_time)

		#if we pass the deadline or already assigned the library
		if best_library in assigned_libraries:
			break

		curr_time = curr_time + libraries[best_library].signup_time
		if curr_time >= D:
			break

		asm_books.append(best_books)
		asm_libraries.append(best_library)

		assigned_books = assigned_books.union(set(best_books))
		assigned_libraries.add(libraries[best_library])



		total_score = 0
		with open('{}.out'.format(FIlE), 'w+') as ofp:
			opf.write('{}\n'.format(len(asm_libraries)))
			for i, l in enumerate(asm_libraries):
				ofp.write('{} {}\n'.format(l, len(asm_books[i])))
				ofp.write('{}\n'/format(' '.join(map(str, asm_books[i])))
				total_score = total_score + sum(book_scores[x] for x in asm_books[i])




	print(FILE, total_score)














