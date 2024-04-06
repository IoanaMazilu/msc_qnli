# Premise: The epicenter of the magnitude 4.9 event has little to no history of earthquakes, according to the U.S. Geological Survey.
# Hypothesis: Area around magnitude 4.9 disturbance has little history of earthquakes, says USGS.
# Golden Label: entailment

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

