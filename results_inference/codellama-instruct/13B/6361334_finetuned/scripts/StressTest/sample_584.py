books_bought_premise = 65
books_bought_hypothesis = 65

# the hypothesis refers to the number of books bought and the amount spent, both mentioned in the premise
if books_bought_hypothesis <= books_bought_premise:
    # check if the estimate of 'books_bought_hypothesis' contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
