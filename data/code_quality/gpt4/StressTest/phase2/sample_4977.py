economics_class_roster_premise = 26
marketing_class_roster_premise = 26
statistics_class_roster_premise = 18

economics_class_roster_hypothesis = 76
marketing_class_roster_hypothesis = 26
statistics_class_roster_hypothesis = 18

# the hypothesis refers to the number of students in each class mentioned in the premise
if economics_class_roster_premise > economics_class_roster_hypothesis:
    # check if the estimate of 'economics_class_roster_hypothesis' contradicts the number of students in the economics class in the premise
    label = "contradiction"
elif marketing_class_roster_premise != marketing_class_roster_hypothesis or statistics_class_roster_premise != statistics_class_roster_hypothesis:
    # check if the number of students in the marketing or statistics class in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)