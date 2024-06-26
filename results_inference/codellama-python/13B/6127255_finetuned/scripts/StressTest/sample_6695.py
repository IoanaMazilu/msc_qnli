withdraw_premise = 14000
withdraw_hypothesis = 14000

# the hypothesis refers to the amount John withdraws, which is also mentioned in the premise
if withdraw_hypothesis >= withdraw_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
