# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 80%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 90%?
# Golden Label: neutral

departure_rate_premise = 80
departure_rate_hypothesis = 90

# the hypothesis talks about the on-time departure rate, referenced also in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'departure_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the departure rate
    # any departure rate greater than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

