day_premise = 7
day_hypothesis = 6

# the hypothesis talks about the time of departure of a train, referenced also in the premise
if day_hypothesis <= day_premise:
    # check if the hypothesis value contradicts the estimate of 'day_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days,
    # any number of days greater than 'day_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
