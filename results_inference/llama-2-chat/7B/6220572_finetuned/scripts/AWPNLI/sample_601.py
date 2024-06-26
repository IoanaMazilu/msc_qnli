books_premise = 38.0
taken_books_premise = 10.0
books_hypothesis = 26.0

# the hypothesis refers to the number of books, which is also mentioned in the premise
# compute the number of books in the premise
books_premise = books_premise - taken_books_premise
if books_hypothesis!= books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
