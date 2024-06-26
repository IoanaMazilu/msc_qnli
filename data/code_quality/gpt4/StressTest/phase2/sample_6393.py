oil_per_cylinder_premise = 8
oil_per_cylinder_hypothesis = 7

# the hypothesis talks about the amount of oil per cylinder in George's car, referenced also in the premise
if oil_per_cylinder_premise <= oil_per_cylinder_hypothesis:
    # check if the premise's amount of oil per cylinder contradicts the hypothesis
    label = "contradiction"
elif oil_per_cylinder_premise > oil_per_cylinder_hypothesis:
    # if the premise's value is greater, it does not contradict the hypothesis and can be inferred from it
    label = "entailment"
else:
    # any other case is neutral
    label = "neutral"

print(label)
