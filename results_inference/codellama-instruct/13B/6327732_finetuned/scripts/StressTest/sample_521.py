stations_premise = 18
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the estimate of'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of stations
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
