books_premise = 38.0
books_hypothesis = 26.0

# the hypothesis refers to the number of books on the shelf, which is also mentioned in the premise
# compute the total number of books on the shelf
total_books_premise = books_premise - books_hypothesis
if total_books_premise!= books_hypothesis:
    # check if the number of books on the shelf from the hypothesis contradicts the number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
