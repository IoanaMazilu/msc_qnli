stations_premise = 8
stations_hypothesis = 4

if stations_hypothesis >= stations_premise:
    # check if the estimate of'stations_hypothesis' contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
