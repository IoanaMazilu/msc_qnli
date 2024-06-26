passengers_premise = 2979
passengers_hypothesis = 1979

# the hypothesis talks about the year of the event, referenced also in the premise
if passengers_hypothesis >= passengers_premise:
    # check if the year in the hypothesis contradicts the estimate of less than 'passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the year
    # any year less than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
