paint_cans_premise = 4
paint_cans_hypothesis = 8

# the hypothesis refers to the number of paint cans Diane found enough to paint the room, also mentioned in the premise
if paint_cans_premise >= paint_cans_hypothesis:
    # check if the number of paint cans in the premise contradicts the estimate of less than 'paint_cans_hypothesis' in the hypothesis
    label = "contradiction"
elif paint_cans_premise != paint_cans_hypothesis:
    # the hypothesis gives an estimate for the number of paint cans
    # any number less than 'paint_cans_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
