magnitude_premise = 4.9
magnitude_hypothesis = 4.9

# the hypothesis refers to the earthquake magnitude and its historical context in the area, which is also referenced in the premise
if magnitude_hypothesis != magnitude_premise:
    # check if the earthquake magnitude in the hypothesis contradicts the magnitude reported in the premise
    label = "contradiction"
else:
    # if the earthquake magnitude from the hypothesis does not contradict the premise, it can be inferred as entailment
    label = "entailment"

print(label)
