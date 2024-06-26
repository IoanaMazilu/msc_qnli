economics_class_premise = 24
economics_class_hypothesis = 24
marketing_class_premise = 28
marketing_class_hypothesis = 28
statistics_class_premise = 18
statistics_class_hypothesis = 18

# the hypothesis talks about the number of students in each of Professor Wang's classes, which is also mentioned in the premise
if economics_class_hypothesis > economics_class_premise:
    # check if the number of students in the economics class in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise:
    # check if the number of students in the marketing class in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
elif statistics_class_hypothesis != statistics_class_premise:
    # check if the number of students in the statistics class in the hypothesis contradicts the number of students mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"

print(label)
