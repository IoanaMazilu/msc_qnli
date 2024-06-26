temperature_premise = 5/9 * (K-32)
temperature_hypothesis = 4/9 * (K-32)

if temperature_premise <= temperature_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
