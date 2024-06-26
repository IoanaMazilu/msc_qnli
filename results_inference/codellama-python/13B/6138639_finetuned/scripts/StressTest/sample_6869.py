people_seated_premise = 5
people_seated_hypothesis = 5

# the hypothesis refers to the number of people seated on a bench mentioned in the premise
if people_seated_hypothesis >= people_seated_premise:
    # check if the estimate of 'people_seated_hypothesis' contradicts the number of people seated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
