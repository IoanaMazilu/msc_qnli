ratio_premise = 3
ratio_hypothesis = 4

# the hypothesis refers to the ratio of ages between Arun and Deepak, both mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
