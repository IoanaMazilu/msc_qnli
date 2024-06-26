# Define variables for the numerical entities in the premise and hypothesis
average_speed_premise = 76
tom_speed_hypothesis = 36

# Check if the hypothesis value contradicts the premise estimate
if average_speed_premise > tom_speed_hypothesis:
    # The hypothesis value contradicts the premise estimate, so the label is contradiction
    label = "contradiction"
elif average_speed_premise <= tom_speed_hypothesis:
    # The hypothesis value is consistent with the premise estimate, so the label is neutral
    label = "neutral"
else:
    # The premise only gives an estimate, so we cannot infer entailment
    label = "neutral"

print(label)
