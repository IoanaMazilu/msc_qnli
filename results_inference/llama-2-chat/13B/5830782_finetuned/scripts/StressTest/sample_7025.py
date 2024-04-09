speed_premise = 30
speed_hypothesis = 10

# the hypothesis refers to the speed of Cara's drive mentioned in the premise
if speed_premise!= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
