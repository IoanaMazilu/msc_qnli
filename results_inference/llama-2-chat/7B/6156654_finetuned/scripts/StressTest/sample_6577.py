shirts_bought_premise = 560
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts Vijay bought, which is also mentioned in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif shirts_bought_hypothesis < shirts_bought_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
