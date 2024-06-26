arun_deepak_ratio_premise = 4/5
arun_deepak_ratio_hypothesis = 4/5

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise < arun_deepak_ratio_hypothesis:
    # check if the ratio in 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif arun_deepak_ratio_premise > arun_deepak_ratio_hypothesis:
    # check if the ratio in 'arun_deepak_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
