bookshelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_premise = bookshelves_premise * books_per_shelf_premise
books_hypothesis = 2251.0

# the hypothesis refers to the total number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_hypothesis = bookshelves_premise * books_per_shelf_premise
if total_books_hypothesis!= total_books_premise:
    # check if the number of books from the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
