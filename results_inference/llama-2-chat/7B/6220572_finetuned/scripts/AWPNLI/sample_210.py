book_shelves_premise = 150
books_per_shelf_premise = 15
books_hypothesis = 2250

# the hypothesis refers to the number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = book_shelves_premise * books_per_shelf_premise
if total_books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
