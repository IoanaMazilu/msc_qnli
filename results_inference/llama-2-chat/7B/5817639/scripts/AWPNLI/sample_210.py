bookshelves_premise = 150.0
books_premise = 15.0
bookshelves_hypothesis = 2250.0

# the hypothesis refers to the total number of books, which is also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = bookshelves_premise * books_premise

# check if the number of books in the hypothesis contradicts the number of books from the premise
if total_books_hypothesis!= total_books_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
