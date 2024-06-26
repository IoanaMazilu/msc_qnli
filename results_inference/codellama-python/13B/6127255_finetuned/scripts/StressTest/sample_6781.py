hours_week_premise = 80
hours_week_hypothesis = 30

# the hypothesis refers to the hours of work paid with x dollars per hour, which is also mentioned in the premise
if hours_week_hypothesis >= hours_week_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of less than 'hours_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
