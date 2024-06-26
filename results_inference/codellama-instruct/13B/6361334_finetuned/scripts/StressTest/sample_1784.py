age_premise = 5/3
age_hypothesis = 5/3

# the hypothesis refers to the same ratio of age as the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the ratio of age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
