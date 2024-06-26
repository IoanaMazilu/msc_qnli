amount_premise = 4050
amount_hypothesis = 6050
interest_rate = 6

# the hypothesis refers to the amount from Anwar mentioned in the premise
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
