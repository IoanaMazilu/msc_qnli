week_premise = 2
week_hypothesis = 1

# the hypothesis talks about the number of weeks until the increase in gym visits, referenced also in the premise
if week_hypothesis >= week_premise:
    # check if the hypothesis value contradicts the estimate of less than 'week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
