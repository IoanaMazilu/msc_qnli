amount_premise = 363
amount_hypothesis = 215

# the hypothesis and premise mention the estimated amount needed for Fannie and Freddie
if amount_hypothesis!= amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
