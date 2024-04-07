# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between less than 5 and 2 standard deviations below the mean.
# Golden Label: entailment

lower_bound_premise = 1
upper_bound_premise = 2
lower_bound_hypothesis = 5
upper_bound_hypothesis = 2

# the hypothesis refers to the number of hours Pat watched television, which is also mentioned in the premise
if lower_bound_hypothesis < lower_bound_premise or upper_bound_hypothesis != upper_bound_premise:
    # check if the hypothesis bounds contradict the premise bounds
    label = "contradiction"
elif lower_bound_hypothesis > lower_bound_premise and upper_bound_hypothesis == upper_bound_premise:
    # check if the hypothesis bounds can be explicitly entailed from the premise bounds
    label = "entailment"
else:
    # if the hypothesis bounds do not contradict or can't be explicitly entailed from the premise bounds, we infer neutrality
    label = "neutral"

print(label)

