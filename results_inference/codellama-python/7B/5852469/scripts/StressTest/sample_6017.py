people_class_premise = 20
people_class_hypothesis = 20

# the hypothesis and the premise refer to the same number of people
if people_class_hypothesis!= people_class_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_class_hypothesis <= people_class_premise:
    # check if the estimate of 'people_class_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
