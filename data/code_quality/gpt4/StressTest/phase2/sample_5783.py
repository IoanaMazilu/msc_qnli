speed_premise = 9
speed_hypothesis = 6

# the hypothesis talks about the speed at which Lindy runs, which is also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis is the same as the speed in the premise, it implies entailment
    label = "entailment"

print(label)
