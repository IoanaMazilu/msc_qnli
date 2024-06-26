book_shelves_premise = 150.0
books_per_shelf_premise = 15.0
total_books_premise = book_shelves_premise * books_per_shelf_premise

# The hypothesis refers to the total number of books, which is also mentioned in the premise
hypothesis_books = 2251.0

# Check if the total number of books in the hypothesis contradicts the estimate from the premise
if total_books_premise!= hypothesis_books:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
