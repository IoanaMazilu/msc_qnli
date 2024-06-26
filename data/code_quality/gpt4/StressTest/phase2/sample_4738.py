stations_premise = 86
stations_hypothesis = 16

# the hypothesis mentions the number of stations between two cities, also referenced in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
