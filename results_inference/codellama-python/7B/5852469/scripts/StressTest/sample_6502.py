matthew_walking_rate_premise = 5
johnny_walking_rate_premise = 4
matthew_walking_rate_hypothesis = 3
johnny_walking_rate_hypothesis = 4

# the hypothesis talks about the walking rates of Matthew and Johnny, referenced also in the premise
if johnny_walking_rate_hypothesis <= johnny_walking_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'johnny_walking_rate_premise'
    label = "contradiction"
elif matthew_walking_rate_hypothesis <= matthew_walking_rate_premise:
    # check if the estimate of'matthew_walking_rate_hypothesis' contradicts the number of walking rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rates
    # any number of walking rate greater than'matthew_walking_rate_premise' and 'johnny_walking_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
