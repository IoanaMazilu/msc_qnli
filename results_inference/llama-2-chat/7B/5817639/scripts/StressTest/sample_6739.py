paint_premise = 1
paint_hypothesis = 1

# the hypothesis talks about the number of cans of paint needed to paint a room, referenced also in the premise
if paint_hypothesis <= paint_premise:
    # check if the hypothesis value contradicts the estimate of less than 'paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cans of paint needed
    # any number of cans of paint needed that is consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
