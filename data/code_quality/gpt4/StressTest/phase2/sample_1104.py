participants_premise = 4
participants_hypothesis = 3

# The hypothesis refers to the number of participants in the race, which is also mentioned in the premise
if participants_premise <= participants_hypothesis:
    # Check if the hypothesis value contradicts the exact number of participants in the premise
    label = "contradiction"
elif participants_premise > participants_hypothesis:
    # If the number of participants in the premise is greater than the hypothesis, then it fully and explicitly entails the hypothesis
    label = "entailment"

print(label)
