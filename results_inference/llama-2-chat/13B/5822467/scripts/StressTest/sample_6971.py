stations_premise = 8
stations_hypothesis = 2

# the hypothesis refers to the number of stations between Vijayawada and Chennai mentioned in the premise
if stations_premise <= stations_hypothesis:
    # check if the hypothesis value contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of stations, while the hypothesis gives a lower number
    # any lower number is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
