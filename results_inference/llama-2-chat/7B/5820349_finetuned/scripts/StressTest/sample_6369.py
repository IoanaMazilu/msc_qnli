paint_cans_premise = 4
paint_cans_hypothesis = 8

# the hypothesis refers to the number of paint cans needed to paint one third of the room, mentioned in the premise
if paint_cans_premise >= paint_cans_hypothesis:
    # check if the estimate of 'paint_cans_hypothesis' contradicts the number of paint cans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
