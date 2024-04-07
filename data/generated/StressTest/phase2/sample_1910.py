# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between less than 1 and 2 standard deviations below the mean.
# Golden Label: contradiction

pat_hours_watched_premise_lower = 1
pat_hours_watched_premise_upper = 2
pat_hours_watched_hypothesis_lower = -1
pat_hours_watched_hypothesis_upper = 2

# the hypothesis makes a statement about the number of hours Pat watched television, which is also referred to in the premise
if pat_hours_watched_hypothesis_lower < pat_hours_watched_premise_lower or pat_hours_watched_hypothesis_upper > pat_hours_watched_premise_upper:
    # check if the range of hours Pat watched television according to the hypothesis contradicts the range given in the premise
    label = "contradiction"
elif pat_hours_watched_hypothesis_lower > pat_hours_watched_premise_lower or pat_hours_watched_hypothesis_upper < pat_hours_watched_premise_upper:
    # check if the range of hours Pat watched television according to the hypothesis is within the range given in the premise
    label = "entailment"
else:
    # the ranges are equal so the hypothesis is fully entailed from the premise
    label = "entailment"

print(label)

