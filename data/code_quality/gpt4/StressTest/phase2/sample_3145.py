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
