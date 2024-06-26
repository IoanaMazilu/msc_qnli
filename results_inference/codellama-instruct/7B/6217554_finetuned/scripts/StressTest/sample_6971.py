stations_premise = 8
stations_hypothesis = 2

if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the estimate of more than'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
