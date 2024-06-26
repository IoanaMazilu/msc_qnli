mary_played_premise = [less than 8, 2, 3]
mary_played_hypothesis = [1, 2, 3]

# the hypothesis mentions the same scores as the premise, but with different order
if mary_played_hypothesis == mary_played_premise:
    # the hypothesis is consistent with the premise, but does not provide any additional information
    label = "neutral"
else:
    # the hypothesis mentions different scores in a different order, so it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
