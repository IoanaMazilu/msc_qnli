economics_class_premise = 30
economics_class_hypothesis = 20
marketing_class_premise = 28
marketing_class_hypothesis = 28
statistics_class_premise = 18
statistics_class_hypothesis = 18

# the hypothesis refers to the number of students in each class mentioned in the premise
if economics_class_hypothesis >= economics_class_premise:
    # check if the number of students in economics class in the hypothesis contradicts the premise estimate of less than 30
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise:
    # check if the number of students in marketing class in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif statistics_class_hypothesis != statistics_class_premise:
    # check if the number of students in statistics class in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
