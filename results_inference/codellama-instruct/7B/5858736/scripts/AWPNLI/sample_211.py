book_shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_premise = book_shelves_premise * books_per_shelf_premise

hypothesis_books = 2251.0

if hypothesis_books!= total_books_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
