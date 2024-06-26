scientific_arithmetic_premise = 1/2
scientific_arithmetic_hypothesis = 6/2

# the hypothesis talks about the ratio of the ages of Lewis and Brown, referenced also in the premise
if scientific_arithmetic_hypothesis <= scientific_arithmetic_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif scientific_arithmetic_hypothesis > scientific_arithmetic_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # if the hypothesis value and premise value are equal, it is neutral
    label = "neutral"

print(label)
