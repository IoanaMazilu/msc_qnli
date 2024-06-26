arun_deepak_ratio_premise = 1/4
arun_deepak_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio between the ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the estimate of 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif arun_deepak_ratio_hypothesis > arun_deepak_ratio_premise:
    # if the ratio in the hypothesis is greater than the ratio in the premise, it is entailed
    label = "entailment"
else:
    # if the ratio in the hypothesis is equal to the ratio in the premise, it is neutral
    label = "neutral"

print(label)
