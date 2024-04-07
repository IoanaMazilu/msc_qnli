# Premise: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had 20 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Hypothesis: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had less than 30 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Golden Label: entailment

econ_class_premise = 20
econ_class_hypothesis = 30
marketing_class_premise = 28
marketing_class_hypothesis = 28
stats_class_premise = 18
stats_class_hypothesis = 18

# the hypothesis refers to the number of students in each class, as mentioned in the premise
if econ_class_hypothesis < econ_class_premise:
    # check if the estimate of 'econ_class_hypothesis' contradicts the number of students in the economics class in the premise
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise:
    # check if the number of students in the marketing class in the hypothesis contradicts the number of students in the marketing class reported in the premise
    label = "contradiction"
elif stats_class_hypothesis != stats_class_premise:
    # check if the number of students in the statistics class in the hypothesis contradicts the number of students in the statistics class reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

