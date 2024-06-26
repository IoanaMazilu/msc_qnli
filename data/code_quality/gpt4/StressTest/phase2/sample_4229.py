speed_premise = 30
speed_hypothesis = 30

# the hypothesis talks about the speed at which Cara drives from City A to City B, also mentioned in the premise
if speed_hypothesis < speed_premise:
    # check if the speed in the hypothesis contradicts the speed stated in the premise
    label = "contradiction"
elif speed_hypothesis > speed_premise:
    # check if the speed in the hypothesis contradicts the speed stated in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
