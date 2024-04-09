raman_butter_premise = 47
raman_butter_hypothesis = 27

# the hypothesis refers to the amount of butter mixed in the premise
if raman_butter_premise > raman_butter_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif raman_butter_hypothesis > raman_butter_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the premise and hypothesis values are equal, so the relation is neutral
    label = "neutral"

print(label)
