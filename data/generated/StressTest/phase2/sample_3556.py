# Premise: The number of hours that Pat, a resident of Town X, watched television last week was between less than 6 and 2 standard deviations below the mean.
# Hypothesis: The number of hours that Pat, a resident of Town X, watched television last week was between 1 and 2 standard deviations below the mean.
# Golden Label: neutral

hours_tv_watched_premise = 6
hours_tv_watched_hypothesis = 1

# the hypothesis talks about the number of hours Pat watched TV, which is also referenced in the premise
if hours_tv_watched_hypothesis >= hours_tv_watched_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_tv_watched_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_tv_watched_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

