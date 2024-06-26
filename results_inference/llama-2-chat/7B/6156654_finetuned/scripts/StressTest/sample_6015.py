jane_age_premise = 20
jane_age_hypothesis = 40

# the hypothesis refers to Jane's age when she started baby-sitting, which is also mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is a logical consequence and not contradictory
    # however, it cannot be explicitly entailed from the premise, so the label is neutral
    label = "neutral"

print(label)
