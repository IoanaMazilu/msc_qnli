stations_premise = 15
stations_hypothesis = 75

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of 15 stations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations greater than 15 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
