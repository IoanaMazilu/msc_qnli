arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 5/3

# the hypothesis is about the ratio between the ages of Arun and Deepak, which is also mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif arun_deepak_ratio_hypothesis > arun_deepak_ratio_premise:
    # check if the ratio in the hypothesis is greater than the ratio mentioned in the premise
    label = "neutral"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
