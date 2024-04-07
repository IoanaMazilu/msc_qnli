# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 40%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 70%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: neutral

departure_rate_premise = 40
departure_rate_hypothesis = 70

# the hypothesis talks about the on-time departure rate from Phoenix,
# which is also mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the on-time departure rate
    # any rate higher than 'departure_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

