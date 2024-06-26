ab_ac_ratio_premise = 1.25
ab_ac_ratio_hypothesis = 1.25
ab_bc_difference_premise = 5
ab_bc_difference_hypothesis = 4

# the hypothesis talks about the ratios of the lengths of sides and differences between sides of a right triangle ABC,
# all of which are also mentioned in the premise

# first, we check if the ratios of lengths of sides AB and AC in the premise and hypothesis contradict each other
if ab_ac_ratio_premise != ab_ac_ratio_hypothesis:
    label = "contradiction"
# then, we check if the difference in lengths of sides AB and BC in the hypothesis contradicts the premise
elif ab_bc_difference_hypothesis > ab_bc_difference_premise:
    label = "contradiction"
# if neither of those conditions is met, we check if the hypothesis can be fully entailed from the premise
elif ab_bc_difference_hypothesis < ab_bc_difference_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
