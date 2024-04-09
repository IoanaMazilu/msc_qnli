total_weight_premise = 42.0
weight_per_book_premise = 3.0
total_books_hypothesis = 14.0

# the hypothesis refers to the number of books, which can be inferred from the premise
# compute the total number of books in the premise
total_books_premise = total_weight_premise / weight_per_book_premise
if total_books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
