pat_tv_hours_lower_bound_premise = 1
pat_tv_hours_upper_bound_premise = 2
pat_tv_hours_lower_bound_hypothesis = 6
pat_tv_hours_upper_bound_hypothesis = 2

# the hypothesis refers to the range of hours that Pat watched TV, which is also mentioned in the premise
if pat_tv_hours_lower_bound_hypothesis < pat_tv_hours_lower_bound_premise or pat_tv_hours_upper_bound_hypothesis > pat_tv_hours_upper_bound_premise:
    # check if the range in the hypothesis contradicts the range given in the premise
    label = "contradiction"
elif pat_tv_hours_lower_bound_hypothesis > pat_tv_hours_lower_bound_premise or pat_tv_hours_upper_bound_hypothesis < pat_tv_hours_upper_bound_premise:
    # check if the range in the hypothesis is completely contained within the range given in the premise
    label = "entailment"
else:
    # if the range in the hypothesis overlaps but is not completely contained within the range given in the premise, we can infer neutrality
    label = "neutral"

print(label)
