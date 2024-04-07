# Premise: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had less than 76 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Hypothesis: When Professor Wang looked at the rosters for this term's classes, she saw that the roster for her economics class (E) had 16 names, the roster for her marketing class (M) had 28, and the roster for her statistics class (S) had 18.
# Golden Label: neutral

econ_class_premise = 76
econ_class_hypothesis = 16
marketing_class_premise = 28
marketing_class_hypothesis = 28
stats_class_premise = 18
stats_class_hypothesis = 18

# the hypothesis refers to the number of students in three different classes mentioned in the premise
if econ_class_hypothesis >= econ_class_premise:
    # check if the number of students in the economics class in the hypothesis contradicts the estimate less than 'econ_class_premise'
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise or stats_class_hypothesis != stats_class_premise:
    # check if the number of students in the marketing and statistics classes in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

