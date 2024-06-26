paint_premise = 8
paint_hypothesis = 4

# the hypothesis talks about the number of cans of paint needed to paint one third of Diane's room
if paint_hypothesis <= paint_premise:
    # check if the hypothesis value contradicts the estimate of 'paint_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of cans of paint needed, and the hypothesis value is consistent with it
    label = "neutral"

print(label)
