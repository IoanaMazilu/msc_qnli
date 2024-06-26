paint_cans_premise = 4
paint_cans_hypothesis = 8

# the hypothesis refers to the number of paint cans needed to paint one third of the room, mentioned in the premise
if paint_cans_premise >= paint_cans_hypothesis:
    # check if the number of 'paint_cans_premise' contradicts the estimate of less than 'paint_cans_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
