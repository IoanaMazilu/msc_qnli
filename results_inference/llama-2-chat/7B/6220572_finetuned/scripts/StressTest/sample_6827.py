age_ratio_premise = 4/3
age_ratio_hypothesis = 1/3

# the hypothesis refers to the ratio between the ages of Arun and Deepak mentioned in the premise
if age_ratio_premise == age_ratio_hypothesis:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
