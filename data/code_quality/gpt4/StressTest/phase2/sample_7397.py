speed_premise = 60
speed_hypothesis = 70

# the hypothesis talks about the driving speed from town R to town B, mentioned also in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    label = "entailment"

print(label)
