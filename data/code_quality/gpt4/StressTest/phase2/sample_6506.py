speed_premise = 40
speed_hypothesis = 10

# the hypothesis talks about the speed of Bob's drive from City A to City B, referenced also in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)