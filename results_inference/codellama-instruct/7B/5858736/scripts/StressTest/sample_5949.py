temperature_premise = 5/9 * (K-32)
temperature_hypothesis = 2/9 * (K-32)

if temperature_premise <= temperature_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
