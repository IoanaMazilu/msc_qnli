stations_premise = 22
stations_hypothesis = 12

# the hypothesis refers to the number of stations between Ernakulam and Chennai, just like the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise of having less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
