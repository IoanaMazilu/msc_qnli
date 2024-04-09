paint_can_premise = 1
paint_can_hypothesis = 1

# the hypothesis refers to the amount of paint Diane uses to paint one third of her room, mentioned in the premise
if paint_can_hypothesis >= paint_can_premise:
    # check if the hypothesis value contradicts the premise that Diane uses less than 'paint_can_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
