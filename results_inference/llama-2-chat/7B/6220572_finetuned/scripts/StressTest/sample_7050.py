share_premise = 1300
share_hypothesis = 4300

# the hypothesis refers to the share of Deepak mentioned in the premise
if share_hypothesis <= share_premise:
    # check if the estimate of'share_hypothesis' contradicts the share of Deepak in the premise
    label = "contradiction"
else:
    # any share greater than'share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
