stations_premise = 15
stations_hypothesis = 75

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the number of stations in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of stations between Hyderabad and Bangalore
    # any number of stations greater than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
