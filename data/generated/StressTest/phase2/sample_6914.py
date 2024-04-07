# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 70%?
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%?
# Golden Label: contradiction

departure_rate_premise = 70
departure_rate_hypothesis = 50

# the hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis > departure_rate_premise:
    # check if the hypothesis value contradicts the estimated on-time departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis < departure_rate_premise:
    # check if the hypothesis value is less than the estimated on-time departure rate in the premise
    label = "entailment"
else:
    # if the hypothesis value and the premise value are equal, we can infer entailment
    label = "entailment"

print(label)

