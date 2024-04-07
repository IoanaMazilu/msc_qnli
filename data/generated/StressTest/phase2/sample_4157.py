# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between 2 and 2 standard deviations below the mean.
# Golden Label: contradiction

pat_hours_watched_min_premise = 1
pat_hours_watched_max_premise = 2
pat_hours_watched_min_hypothesis = 2
pat_hours_watched_max_hypothesis = 2

# the hypothesis refers to the number of hours Pat watched television, which is also referenced in the premise
if pat_hours_watched_min_hypothesis >= pat_hours_watched_max_premise:
    # check if the minimum hours watched in the hypothesis contradict the maximum hours watched in the premise
    label = "contradiction"
elif pat_hours_watched_max_hypothesis != pat_hours_watched_max_premise:
    # check if the maximum hours watched in the hypothesis contradict the maximum hours watched in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we have a neutral situation
    label = "neutral"

print(label)

