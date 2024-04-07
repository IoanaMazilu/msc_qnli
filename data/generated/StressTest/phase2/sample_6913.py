# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than less than 80%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 70%?
# Golden Label: neutral

departure_rate_premise = 80
departure_rate_hypothesis = 70

# the hypothesis refers to the on-time departure rate from the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the requirement of being more than 'departure_rate_premise'
    label = "contradiction"
elif departure_rate_hypothesis == departure_rate_premise:
    # if the hypothesis requirement is exactly the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis requirement is less than the one in the premise, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

