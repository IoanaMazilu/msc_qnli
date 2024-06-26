amount_premise = 363
amount_hypothesis = 215

# the hypothesis and premise mention the amount of money needed by Fannie and Freddie
if amount_hypothesis < amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis is greater or equal to the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
