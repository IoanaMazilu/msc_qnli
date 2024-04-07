# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 20%?
# Golden Label: entailment

departure_rate_premise = 60
departure_rate_hypothesis = 20

# the hypothesis talks about the on-time departure rate from Phoenix, which is also referenced in the premise 
if departure_rate_hypothesis > departure_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # the premise gives a higher departure rate
    # a lower departure rate in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the departure rate in the premise is equal to the one in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

