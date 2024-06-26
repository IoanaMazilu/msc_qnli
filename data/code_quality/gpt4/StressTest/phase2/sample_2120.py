econ_class_premise = 20
econ_class_hypothesis = 20
marketing_class_premise = 28
marketing_class_hypothesis = 28
statistics_class_premise = 18
statistics_class_hypothesis = 18

# the hypothesis refers to the number of students in each class, as mentioned in the premise
if econ_class_hypothesis <= econ_class_premise:
    # check if the hypothesis value contradicts the estimate of more than 'econ_class_premise'
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise or statistics_class_hypothesis != statistics_class_premise:
    # check if the number of students in the marketing or statistics class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
