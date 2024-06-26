books_premise = 35
books_bought_premise = 56
books_hypothesis = 92

# the hypothesis refers to the total number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = books_premise + books_bought_premise
if books_hypothesis!= total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
