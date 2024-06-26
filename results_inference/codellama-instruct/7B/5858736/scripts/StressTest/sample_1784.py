age_premise = 5/3
age_hypothesis = 5/3

# the hypothesis refers to the age difference between the two individuals
if age_premise <= age_hypothesis:
    # check if the estimate of 'age_hypothesis' contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
