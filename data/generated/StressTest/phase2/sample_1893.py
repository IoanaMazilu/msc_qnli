# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between less than 4 and 2 standard deviations below the mean.
# Golden Label: entailment

pat_tv_hours_lower_bound_premise = 1
pat_tv_hours_upper_bound_premise = 2
pat_tv_hours_lower_bound_hypothesis = 4
pat_tv_hours_upper_bound_hypothesis = 2

# the hypothesis refers to the number of hours Pat watched television last week, which is also mentioned in the premise
if pat_tv_hours_lower_bound_hypothesis < pat_tv_hours_lower_bound_premise or pat_tv_hours_upper_bound_hypothesis > pat_tv_hours_upper_bound_premise:
    # check if the hypothesis values contradict the range of hours Pat watched television according to the premise
    label = "contradiction"
elif pat_tv_hours_lower_bound_hypothesis == pat_tv_hours_lower_bound_premise and pat_tv_hours_upper_bound_hypothesis == pat_tv_hours_upper_bound_premise:
    # if the hypothesis values are exactly the same as the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values do not contradict or exactly match the premise ones, we infer neutrality
    label = "neutral"

print(label)

