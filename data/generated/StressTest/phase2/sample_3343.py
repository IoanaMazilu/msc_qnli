# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 40%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 60%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: neutral

departure_rate_premise = 40
departure_rate_hypothesis = 60

# the hypothesis refers to the departure rate mentioned in the premise
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # if the departure rate in the hypothesis is greater than the departure rate in the premise, it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

