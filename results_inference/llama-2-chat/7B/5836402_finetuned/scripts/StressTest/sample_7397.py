speed_premise = 60
speed_hypothesis = 70

# the hypothesis talks about the speed at which Tom drives from town R to town B, which is also mentioned in the premise
if speed_hypothesis!= speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
