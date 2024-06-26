gang_premise = 8
gang_hypothesis = 3

# the hypothesis talks about the number of gangs Andrew has, referenced also in the premise
if gang_premise <= gang_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
