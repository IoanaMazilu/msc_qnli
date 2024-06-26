amount_premise = 5887
amount_hypothesis = 5887

# the hypothesis makes the same claim as the premise, but with a different amount
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the hypothesis does not make any claims that contradict the premise, but it also doesn't provide any new information that can be entailed from the premise
    label = "neutral"

print(label)
