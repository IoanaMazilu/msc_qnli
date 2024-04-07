# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 90%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 80%?
# Golden Label: entailment

departure_rate_premise = 90
departure_rate_hypothesis = 80

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis departure rate contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the hypothesis departure rate contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates are equal to the premise ones, we can infer entailment
    label = "entailment"

print(label)

