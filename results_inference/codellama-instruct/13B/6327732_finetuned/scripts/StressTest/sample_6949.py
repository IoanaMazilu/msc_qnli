age_ratio_premise = 1/4
age_ratio_hypothesis = 5/4

# the hypothesis refers to the ratio between the ages of Arun and Deepak mentioned in the premise
if age_ratio_premise <= age_ratio_hypothesis:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio between the ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
