# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 40%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 70%?
# Golden Label: contradiction

departure_rate_premise = 40
departure_rate_hypothesis = 70

# the hypothesis talks about the on-time departure rate, which is also referenced in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesized departure rate contradicts the premise's departure rate
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any on-time departure rate greater than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

