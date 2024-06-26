# the hypothesis talks about the ratio of distances between A to B and B to C, referenced also in the premise
if (distance_AB / distance_BC) <= (4 / 2):
    # check if the hypothesis value contradicts the estimate of more than '1:2'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of distances between A to B and B to C
    # any ratio greater than '1:2' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
