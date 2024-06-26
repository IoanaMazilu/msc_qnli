books_premise = 14.0
books_hypothesis = 14.0

# the hypothesis refers to the number of books, which is also mentioned in the premise
if books_hypothesis!= books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
