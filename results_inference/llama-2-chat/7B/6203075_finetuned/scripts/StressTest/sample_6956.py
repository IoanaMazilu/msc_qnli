average_shirts_premise = 40
average_shirts_hypothesis = 40
purchased_shirts_premise = 8
purchased_shirts_hypothesis = 8

# the hypothesis talks about the average number of shirts each person has, which is also mentioned in the premise
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
