people_class_premise = 20
people_class_hypothesis = 20

# the hypothesis refers to the number of people in the class, which is also mentioned in the premise
if people_class_hypothesis <= people_class_premise:
    # check if the estimate of 'people_class_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
