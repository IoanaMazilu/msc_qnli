# Premise: Diane find 1 can of paint are just enough to paint one third of her room.
# Hypothesis: Diane find less than 2 can of paint are just enough to paint one third of her room.
# Golden Label: entailment

paint_can_premise = 1
paint_can_hypothesis = 2

# the hypothesis refers to the number of paint cans needed to paint a third of the room, mentioned also in the premise
if paint_can_hypothesis <= paint_can_premise:
    # check if the hypothesis value contradicts the number of paint cans reported in the premise
    label = "contradiction"
else:
    # the premise states an exact number of paint cans needed
    # any number of paint cans less than 'paint_can_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

