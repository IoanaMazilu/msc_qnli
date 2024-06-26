paint_premise = 4
paint_hypothesis = 8

# the hypothesis talks about the number of cans of paint needed to paint a room, referenced also in the premise
if paint_hypothesis <= paint_premise:
    # check if the hypothesis value contradicts the estimate of 'paint_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of cans of paint needed to paint a room, but the hypothesis value is greater than that estimate
    # therefore, the hypothesis cannot be explicitly entailed from the premise, but it does not contradict it either
    label = "neutral"

print(label)
