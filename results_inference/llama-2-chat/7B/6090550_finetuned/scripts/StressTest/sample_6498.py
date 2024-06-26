distance_matthew_premise = 45
distance_matthew_hypothesis = 35

# the hypothesis refers to the distance Matthew walked, which is also mentioned in the premise
if distance_matthew_premise <= distance_matthew_hypothesis:
    # check if the distance Matthew walked in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis is greater than the distance in the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise, so the relation is neutral
    label = "neutral"

print(label)
