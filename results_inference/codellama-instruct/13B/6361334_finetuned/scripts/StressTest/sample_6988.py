age_ratio_premise = 2/3
age_ratio_hypothesis = 7/3

# the hypothesis refers to the ratio of the ages of Anil and his son at present, mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
