amount_premise = 7.15
amount_hypothesis = 7.2

# the hypothesis and premise mention the amount Nestle pays to Starbucks
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
