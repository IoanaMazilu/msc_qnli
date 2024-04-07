# Premise: The sides of right triangle ABC are such that the length of side AC is 1.25 times the length of side AB, which itself is 4 units more than the length of side BC.
# Hypothesis: The sides of right triangle ABC are such that the length of side AC is 1.25 times the length of side AB, which itself is more than 4 units more than the length of side BC.
# Golden Label: contradiction

AC_AB_ratio_premise = 1.25
AC_AB_ratio_hypothesis = 1.25
AB_BC_difference_premise = 4
AB_BC_difference_hypothesis = 4

# the hypothesis refers to the ratio of sides AC to AB and the difference between sides AB and BC mentioned in the premise
if AC_AB_ratio_premise != AC_AB_ratio_hypothesis:
    # check if the ratio of sides AC to AB in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif AB_BC_difference_hypothesis > AB_BC_difference_premise:
    # check if the difference between sides AB and BC in the hypothesis contradicts the difference in the premise
    label = "contradiction"
elif AC_AB_ratio_premise == AC_AB_ratio_hypothesis and AB_BC_difference_hypothesis == AB_BC_difference_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # remaining possibility is neutrality
    label = "neutral"

print(label)

