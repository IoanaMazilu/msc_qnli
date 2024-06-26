miles_traveled_premise = 160
miles_traveled_hypothesis = 260

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, mentioned also in the premise
if miles_traveled_premise != miles_traveled_hypothesis:
    # check if the distance traveled in the hypothesis contradicts the distance traveled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
