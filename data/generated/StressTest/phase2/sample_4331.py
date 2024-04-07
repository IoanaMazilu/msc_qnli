# Premise: Diane find 6 cans of paint are just enough to paint one third of her room.
# Hypothesis: Diane find 2 cans of paint are just enough to paint one third of her room.
# Golden Label: contradiction

paint_cans_premise = 6
paint_cans_hypothesis = 2

# the hypothesis refers to the number of paint cans needed to paint one third of the room, mentioned in the premise
if paint_cans_hypothesis == paint_cans_premise:
    # check if the hypothesis value is the same as the premise value
    label = "entailment"
else:
    # if the hypothesis value is not the same as the premise value, it contradicts the premise
    label = "contradiction"

print(label)

