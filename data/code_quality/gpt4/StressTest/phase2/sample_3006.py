economics_class_premise = 24
economics_class_hypothesis = 64
marketing_class_premise = 28
marketing_class_hypothesis = 28
statistics_class_premise = 18
statistics_class_hypothesis = 18

# the hypothesis refers to the number of students in the economics, marketing and statistics classes mentioned in the premise
if economics_class_premise > economics_class_hypothesis:
    # check if the number of students in the economics class in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif marketing_class_premise != marketing_class_hypothesis:
    # check if the number of students in the marketing class in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif statistics_class_premise != statistics_class_hypothesis:
    # check if the number of students in the statistics class in the premise contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
