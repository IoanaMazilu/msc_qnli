speed_premise = 30
speed_hypothesis = 20

# the hypothesis refers to Alice's driving speed, stated also in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speed matches the premise speed, we can infer entailment
    label = "entailment"

print(label)
