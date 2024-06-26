books_bought_premise = 6
books_bought_hypothesis = 60

# the hypothesis refers to the number of books bought mentioned in the premise
if books_bought_premise >= books_bought_hypothesis:
    # check if the number of books bought in the premise contradicts the estimate of less than 'books_bought_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
