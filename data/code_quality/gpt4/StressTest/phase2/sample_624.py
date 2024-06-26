people_premise = 6
people_hypothesis = 1

# the hypothesis refers to the number of people Ahok will arrange, as mentioned in the premise
if people_premise <= people_hypothesis:
    # check if the hypothesis value contradicts the exact number of people in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis is less than the number of people in the premise, it does not contradict it but cannot be directly inferred either
    label = "neutral"

print(label)
