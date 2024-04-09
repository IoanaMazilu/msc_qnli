more_weeks_premise = 2
more_weeks_hypothesis = 1

# the hypothesis talks about the number of weeks until Rikki increases her gym visits, referenced also in the premise
if more_weeks_hypothesis >= more_weeks_premise:
    # check if the hypothesis value contradicts the estimate of less than'more_weeks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than'more_weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
