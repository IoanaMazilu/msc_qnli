books_bought_premise = 6
books_bought_hypothesis = 60

# the hypothesis refers to the number of books bought by Jithin mentioned in the premise
if books_bought_hypothesis >= books_bought_premise:
    # check if the estimate of 'books_bought_hypothesis' contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
