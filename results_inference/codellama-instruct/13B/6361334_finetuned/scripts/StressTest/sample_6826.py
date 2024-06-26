age_ratio_premise = 3
age_ratio_hypothesis = 4

# the hypothesis refers to the ratio between the ages of Arun and Deepak, mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)