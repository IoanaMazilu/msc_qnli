arun_age_ratio_premise = 3/3
arun_age_ratio_hypothesis = 4/3

# the hypothesis refers to the ratio of the ages of Arun and Deepak mentioned in the premise
if arun_age_ratio_hypothesis <= arun_age_ratio_premise:
    # check if the estimate of 'arun_age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
elif arun_age_ratio_hypothesis > arun_age_ratio_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
