cans_paint_premise = 4
cans_paint_hypothesis = 8

# the hypothesis talks about the number of cans of paint needed to paint one third of the room
if cans_paint_hypothesis <= cans_paint_premise:
    # check if the hypothesis value contradicts the estimate of 'cans_paint_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of cans of paint needed
    # any number of cans greater than 'cans_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
