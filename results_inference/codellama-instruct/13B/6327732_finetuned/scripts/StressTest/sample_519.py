stations_premise = 18
stations_hypothesis = 58

# the hypothesis talks about the number of stations between Hyderabad and Bangalore
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the number of stations in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of stations
    # any number of stations less than'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)