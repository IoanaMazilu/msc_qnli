speed_premise = 30
speed_hypothesis = 20

if speed_hypothesis >= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
