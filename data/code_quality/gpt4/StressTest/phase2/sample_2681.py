tickets_bought_premise = 10
tickets_bought_hypothesis = 10

# the hypothesis refers to the number of tickets bought by Martin, mentioned in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis contradicts the premise about the number of tickets bought
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)
