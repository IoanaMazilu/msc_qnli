hours_premise = 6
hours_hypothesis = 1

# the hypothesis refers to the number of hours it takes to clean the entire house, mentioned in the premise
if hours_hypothesis <= hours_premise:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
