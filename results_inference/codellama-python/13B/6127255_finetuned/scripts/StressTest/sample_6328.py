cigarettes_per_minute_premise = 20
cigarettes_per_minute_hypothesis = 10

# the hypothesis talks about the number of boxes of cigarettes Kramer can pack per minute, referenced also in the premise
if cigarettes_per_minute_hypothesis >= cigarettes_per_minute_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cigarettes_per_minute_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes of cigarettes Kramer can pack per minute
    # any number of boxes less than 'cigarettes_per_minute_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
