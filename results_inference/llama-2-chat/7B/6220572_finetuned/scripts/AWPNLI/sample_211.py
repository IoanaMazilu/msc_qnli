total_books_premise = book_shelves_premise * books_per_shelf_premise
total_books_hypothesis = 2251.0

# check if the total number of books from the hypothesis contradicts the total number of books from the premise
if total_books_hypothesis!= total_books_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
