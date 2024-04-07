# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 70%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 80%?
# Golden Label: neutral

departure_rate_premise = 70
departure_rate_hypothesis = 80

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # the 'departure_rate_hypothesis' is higher than 'departure_rate_premise'
    # the premise only specifies a rate higher than 70% without giving a maximum limit
    # hence, we can't infer entailment or contradiction
    label = "neutral"

print(label)
