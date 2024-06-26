withdraw_amount_premise = 14000
withdraw_amount_hypothesis = 44000

# the hypothesis refers to the amount John withdraws after 8 months, mentioned in the premise
if withdraw_amount_hypothesis <= withdraw_amount_premise:
    # check if the hypothesis value contradicts the amount of withdrawal in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
