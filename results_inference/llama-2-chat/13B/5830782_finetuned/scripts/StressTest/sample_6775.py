ratio_premise = 1/2
ratio_hypothesis = 4/2

# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
