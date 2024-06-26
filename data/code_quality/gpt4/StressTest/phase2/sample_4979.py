economics_class_premise = 26
economics_class_hypothesis = 66
marketing_class_premise = 26
marketing_class_hypothesis = 26
statistics_class_premise = 18
statistics_class_hypothesis = 18

# the hypothesis refers to the number of students in classes E, M, S mentioned in the premise
if economics_class_premise != economics_class_hypothesis:
    # check if the number of students in the economics class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif marketing_class_premise != marketing_class_hypothesis:
    # check if the number of students in the marketing class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif statistics_class_premise != statistics_class_hypothesis:
    # check if the number of students in the statistics class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
