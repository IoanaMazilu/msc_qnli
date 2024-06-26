stations_premise = 8
stations_hypothesis = 4

# the hypothesis refers to the number of stations between Vijayawada and Chennai, which is also mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of more than'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
