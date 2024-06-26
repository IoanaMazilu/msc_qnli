sheep_horses_premise = 6
sheep_horses_hypothesis = 7

# the hypothesis talks about the ratio of sheep and horses, which is also mentioned in the premise
if sheep_horses_hypothesis <= sheep_horses_premise:
    # check if the hypothesis value contradicts the estimate of less than'sheep_horses_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep and horses
    # any ratio less than'sheep_horses_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
