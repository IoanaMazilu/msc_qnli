paint_can_premise = 1
paint_can_hypothesis = 2

# the hypothesis refers to the number of paint cans needed to paint one third of the room
if paint_can_hypothesis <= paint_can_premise:
    # check if the hypothesis value contradicts the exact number of 'paint_can_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of paint cans needed
    # any number less than 'paint_can_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
