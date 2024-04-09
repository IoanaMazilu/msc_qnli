stations_premise = 85
stations_hypothesis = 25

# the hypothesis refers to the number of stations between Delhi and Chennai mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of'stations_hypothesis' contradicts the estimate of less than'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
