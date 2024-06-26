paint_premise = 2
paint_hypothesis = 1

# the hypothesis talks about the amount of paint needed to paint one third of the room, referenced also in the premise
if paint_hypothesis >= paint_premise:
    # check if the hypothesis value contradicts the estimate of less than 'paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of paint
    # any amount of paint less than 'paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
