stations_premise = 18
stations_hypothesis = 58

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
