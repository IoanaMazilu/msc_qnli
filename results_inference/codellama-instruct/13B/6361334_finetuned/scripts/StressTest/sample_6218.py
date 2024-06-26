stations_premise = 25
stations_hypothesis = 55

# the hypothesis refers to the number of stations between Delhi and Chennai, mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the number of stations in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of stations
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
