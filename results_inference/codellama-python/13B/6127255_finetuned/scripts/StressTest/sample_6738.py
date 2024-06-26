paint_premise = 1
paint_hypothesis = 2

# the hypothesis refers to the amount of paint needed to paint one third of the room, mentioned in the premise
if paint_hypothesis <= paint_premise:
    # check if the hypothesis value contradicts the amount of paint stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
