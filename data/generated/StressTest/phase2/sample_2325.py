# Premise: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had 16 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Hypothesis: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had less than 76 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Golden Label: entailment

economics_class_premise = 16
marketing_class_premise = 28
statistics_class_premise = 18

economics_class_hypothesis = 76
marketing_class_hypothesis = 28
statistics_class_hypothesis = 18

# the hypothesis refers to the number of students in the economics, marketing and statistics classes mentioned in the premise
if economics_class_premise >= economics_class_hypothesis:
    # check if the estimate of 'economics_class_hypothesis' contradicts the number of students in the economics class in the premise
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise or statistics_class_hypothesis != statistics_class_premise:
    # check if the number of students in the marketing and statistics classes in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
