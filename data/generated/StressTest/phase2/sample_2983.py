# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between less than 7 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Golden Label: neutral

tv_hours_premise_lower = 7
tv_hours_hypothesis_lower = 1

# the hypothesis and the premise both talk about the number of hours Pat watched television
# the premise indicates that the number of hours is less than 7 and the hypothesis indicates that it is more than 1
if tv_hours_hypothesis_lower >= tv_hours_premise_lower:
    # check if the lower limit given in the hypothesis contradicts the upper limit given in the premise
    label = "contradiction"
else:
    # the premise gives a range for the number of hours Pat watched television
    # the hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

