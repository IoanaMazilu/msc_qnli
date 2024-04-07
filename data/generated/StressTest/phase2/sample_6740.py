# Premise: Diane find 1 can of paint are just enough to paint one third of her room.
# Hypothesis: Diane find less than 1 can of paint are just enough to paint one third of her room.
# Golden Label: contradiction

paint_cans_premise = 1
paint_cans_hypothesis = 1

# the hypothesis refers to the number of paint cans Diane finds to be enough for painting one third of her room, which is also mentioned in the premise
if paint_cans_hypothesis >= paint_cans_premise:
    # check if the hypothesis value contradicts the premise statement
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

