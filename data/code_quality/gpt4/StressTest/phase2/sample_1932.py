speed_premise = 60
speed_hypothesis = 20

# the hypothesis refers to the speed of driving from town T to town B mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the speed in the premise, we can infer entailment
    label = "entailment"

print(label)