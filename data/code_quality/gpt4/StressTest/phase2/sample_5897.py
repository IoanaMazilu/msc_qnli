speed_premise = 20
speed_hypothesis = 10

# the hypothesis gives a speed for A's departure from Delhi that is also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
