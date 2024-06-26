ratio_premise = 4/2
ratio_hypothesis = 3/2

# the hypothesis refers to the ratio of distances between A to B and B to C, which is also mentioned in the premise
if ratio_hypothesis!= ratio_premise:
    # check if the hypothesis value contradicts the ratio of distances in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio of distances that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
