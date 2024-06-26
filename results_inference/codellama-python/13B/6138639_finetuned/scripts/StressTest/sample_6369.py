paint_cans_premise = 4
paint_cans_hypothesis = 8

# the hypothesis talks about the number of paint cans needed to paint one third of the room, referenced also in the premise
if paint_cans_hypothesis <= paint_cans_premise:
    # check if the hypothesis value contradicts the estimate of more than 'paint_cans_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of paint cans
    # any number of paint cans greater than 'paint_cans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
