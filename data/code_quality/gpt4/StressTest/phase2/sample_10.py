driving_hours_premise = 4
driving_hours_hypothesis = 9
driving_rate_premise = 60
driving_rate_hypothesis = 60

# the hypothesis talks about the driving hours and rate from Town X to Town Z, referenced also in the premise
if driving_hours_hypothesis <= driving_hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'driving_hours_premise'
    label = "contradiction"
elif driving_rate_hypothesis != driving_rate_premise:
    # check if the driving rate in the hypothesis contradicts the driving rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving hours
    # any number of driving hours greater than 'driving_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
