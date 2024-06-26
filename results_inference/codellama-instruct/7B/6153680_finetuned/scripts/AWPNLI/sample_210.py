book_shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_hypothesis = 2250.0

# the hypothesis refers to the total number of books, which can be calculated from the premise
total_books_premise = book_shelves_premise * books_per_shelf_premise
if total_books_hypothesis!= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and calculations do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
