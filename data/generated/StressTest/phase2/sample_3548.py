# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 90%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 40%?
# Golden Label: contradiction

departure_rate_premise = 90
departure_rate_hypothesis = 40

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the estimate of 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # any on-time departure rate less than 'departure_rate_premise' is consistent with the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
