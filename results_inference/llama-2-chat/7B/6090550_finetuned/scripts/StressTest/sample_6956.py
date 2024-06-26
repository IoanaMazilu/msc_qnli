average_shirts_premise = 40
average_shirts_hypothesis = 40
shirts_purchased_premise = 8
shirts_purchased_hypothesis = 8

# the hypothesis talks about the average number of shirts each person has after purchasing 8 shirts each
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
