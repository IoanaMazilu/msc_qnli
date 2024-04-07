# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between 7 and 2 standard deviations below the mean.
# Golden Label: contradiction

pat_hours_premise_low = 1
pat_hours_premise_high = 2
pat_hours_hypothesis_low = 7
pat_hours_hypothesis_high = 2

# the hypothesis speaks about the same range of number of hours that Pat watched television last week mentioned in the premise
if pat_hours_hypothesis_low < pat_hours_premise_low or pat_hours_hypothesis_high > pat_hours_premise_high:
    # check if the range of number of hours in the hypothesis contradicts the range of number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis range does not contradict the premise range, we can infer entailment
    label = "entailment"

print(label)

