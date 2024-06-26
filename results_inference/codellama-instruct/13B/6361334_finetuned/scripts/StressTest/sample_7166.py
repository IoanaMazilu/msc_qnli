people_premise = 15
people_hypothesis = 15

# the hypothesis refers to the number of people mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
