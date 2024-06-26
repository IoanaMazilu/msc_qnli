arun_deepak_age_ratio_premise = 5/4
arun_deepak_age_ratio_hypothesis = 1/4

# the hypothesis refers to the ratio of the ages of Arun and Deepak mentioned in the premise
if arun_deepak_age_ratio_premise <= arun_deepak_age_ratio_hypothesis:
    # check if the estimate of 'arun_deepak_age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
elif arun_deepak_age_ratio_hypothesis > arun_deepak_age_ratio_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
