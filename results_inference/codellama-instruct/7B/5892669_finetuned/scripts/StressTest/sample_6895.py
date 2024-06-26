walk_days_premise = 7
walk_days_hypothesis = 3

# the hypothesis talks about the number of days Alice walked, referenced also in the premise
if walk_days_hypothesis >= walk_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'walk_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'walk_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
