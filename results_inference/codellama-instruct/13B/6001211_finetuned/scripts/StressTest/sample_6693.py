withdraw_premise = 14000
withdraw_hypothesis = 44000

# the hypothesis refers to the amount John withdraws after 8 months, which is also mentioned in the premise
if withdraw_hypothesis <= withdraw_premise:
    # check if the hypothesis value contradicts the amount John withdraws in the premise
    label = "contradiction"
elif withdraw_premise > withdraw_hypothesis:
    # check if the amount John withdraws in the premise contradicts the hypothesis value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
