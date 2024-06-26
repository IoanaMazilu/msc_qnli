# Variables representing the on-time departure rate in the premise and hypothesis
departure_rate_premise = 40
departure_rate_hypothesis = 60

# The hypothesis refers to the on-time departure rate mentioned in the premise
if departure_rate_hypothesis < departure_rate_premise:
    # Check if the 'departure_rate_hypothesis' contradicts the departure rate in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # Check if the 'departure_rate_hypothesis' is greater than the departure rate in the premise
    label = "entailment"
else:
    # If the departure rate in the hypothesis is the same as in the premise, the relation is neutral
    label = "neutral"

print(label)