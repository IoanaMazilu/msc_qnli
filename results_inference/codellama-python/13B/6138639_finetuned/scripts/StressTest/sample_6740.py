paint_cans_premise = 1
paint_cans_hypothesis = 1

# the hypothesis talks about the number of paint cans Diane needs to paint one third of her room, referenced also in the premise
if paint_cans_hypothesis >= paint_cans_premise:
    # check if the hypothesis value contradicts the estimate of less than 'paint_cans_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of paint cans
    # any number of paint cans less than 'paint_cans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
