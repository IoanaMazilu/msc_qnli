blue_paint_premise = 16
blue_paint_hypothesis = 36

# the hypothesis talks about the amount of blue paint needed to change the Fuchsia paint, referenced also in the premise
if blue_paint_hypothesis >= blue_paint_premise:
    # check if the hypothesis value contradicts the estimate of 'blue_paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of blue paint needed,
    # any amount of blue paint greater than or equal to 'blue_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
