store_z_premise = 90
store_z_hypothesis = 90

# the hypothesis refers to the value of store_z in the premise
if store_z_premise <= store_z_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif store_z_premise > store_z_hypothesis:
    # check if the premise value entails the hypothesis value
    label = "entailment"
else:
    # if the hypothesis value and premise value are the same, it is neutral
    label = "neutral"

print(label)
