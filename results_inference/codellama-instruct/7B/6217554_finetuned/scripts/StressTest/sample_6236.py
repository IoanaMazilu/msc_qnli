speed_premise = 2
speed_hypothesis = 3

# the hypothesis refers to the speed of Anne mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
