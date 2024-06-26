speed_premise = 60
speed_hypothesis = 70

# the hypothesis refers to the speed of driving from town R to town B, mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
