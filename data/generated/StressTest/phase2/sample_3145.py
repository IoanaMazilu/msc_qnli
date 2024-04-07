# Premise: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than more than 30%? I will see what is the quickest way to solve it then I will provide the explanation.
# Hypothesis: If the next three flights departed on-time, how many subsequent flights need to depart from Phoenix on-time, for the airport's on-time departure rate to be higher than 50%? I will see what is the quickest way to solve it then I will provide the explanation.
# Golden Label: neutral

departure_rate_premise = 30
departure_rate_hypothesis = 50

# the hypothesis refers to the same context as the premise but changes the on-time departure rate
if departure_rate_hypothesis <= departure_rate_premise:
    # check if the hypothesis value contradicts the premise one
    label = "contradiction"
else:
    # the premise's departure rate is lower than the one in the hypothesis
    # this means there is no contradiction, but also the premise does not entail the hypothesis
    label = "neutral"

print(label)

