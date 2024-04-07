# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between less than 4 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Golden Label: neutral

tv_hours_lower_bound_premise = 4
tv_hours_upper_bound_premise = 2
tv_hours_lower_bound_hypothesis = 1
tv_hours_upper_bound_hypothesis = 2

# Both the premise and hypothesis talk about the number of hours Pat watched television last week
# and compare it with the mean in terms of standard deviations
if tv_hours_lower_bound_hypothesis < tv_hours_lower_bound_premise or tv_hours_upper_bound_hypothesis > tv_hours_upper_bound_premise:
    # Check if the range in the hypothesis contradicts the range given in the premise
    label = "contradiction"
elif tv_hours_lower_bound_hypothesis >= tv_hours_lower_bound_premise and tv_hours_upper_bound_hypothesis <= tv_hours_upper_bound_premise:
    # check if the range in the hypothesis is fully entailed from the range in the premise
    label = "entailment"
else:
    # the hypothesis range does not contradict the premise range but cannot be fully entailed from it either
    label = "neutral"

print(label)

