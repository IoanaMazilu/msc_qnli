amount_premise = 7.2
amount_hypothesis = 7.15

# the hypothesis and premise mention the amount of money paid by Nestle to Starbucks
if amount_hypothesis < amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis is greater or equal to the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
