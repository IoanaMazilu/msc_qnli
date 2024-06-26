books_premise = 38.0
books_added_premise = 10.0
total_books_hypothesis = 52.0

# the hypothesis refers to the total number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = books_premise + books_added_premise
if total_books_hypothesis!= total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
