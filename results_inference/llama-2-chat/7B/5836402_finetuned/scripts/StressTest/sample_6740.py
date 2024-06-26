paint_can_premise = 1
paint_can_hypothesis = 1

# the hypothesis talks about the number of paint cans, which is also referenced in the premise
if paint_can_hypothesis >= paint_can_premise:
    # check if the hypothesis value contradicts the estimate of less than 'paint_can_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of paint cans
    # any number of paint cans less than 'paint_can_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
