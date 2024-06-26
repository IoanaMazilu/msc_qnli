innings_premise = 16
innings_hypothesis = 86

# the hypothesis talks about the number of innings of Suraj, referenced also in the premise
if innings_hypothesis == innings_premise:
    # check if the number of innings in the hypothesis exactly matches the number of innings in the premise
    label = "entailment"
elif innings_hypothesis < innings_premise:
    # check if the number of innings in the hypothesis contradicts the number of innings in the premise
    label = "contradiction"
else:
    # the number of innings in the hypothesis is greater than the innings in the premise,
    # as such this doesn't contradict the premise but cannot be explicitly entailed from the premise 
    label = "neutral"

print(label)
