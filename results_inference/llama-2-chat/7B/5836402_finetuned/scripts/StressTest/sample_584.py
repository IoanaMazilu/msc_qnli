books_bought_premise = 65
books_bought_hypothesis = 65

# the hypothesis refers to the number of books bought by Rahim mentioned in the premise
if books_bought_hypothesis <= books_bought_premise:
    # check if the hypothesis value contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
