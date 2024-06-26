speed_premise = 44
speed_hypothesis = 84

# the hypothesis refers to the speed that Ganesh covers from X to Y, also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis equals the speed in the premise, we can infer entailment
    label = "entailment"

print(label)