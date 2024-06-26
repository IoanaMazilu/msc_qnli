share_premise = 500
share_hypothesis = 600

# the hypothesis refers to the share mentioned in the premise
if share_hypothesis <= share_premise:
    # check if the share in the hypothesis contradicts the share in the premise
    label = "contradiction"
else:
    # if the share in the hypothesis is greater than the share in the premise, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
