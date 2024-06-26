people_class_premise = 100
people_class_hypothesis = 100

# the hypothesis refers to the same number of people as the premise
if people_class_hypothesis <= people_class_premise:
    # check if the estimate of 'people_class_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)