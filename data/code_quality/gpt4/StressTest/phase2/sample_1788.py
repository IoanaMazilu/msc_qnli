stations_premise = 12
stations_hypothesis = 22

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_premise > stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than 'stations_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives an upper limit for the number of stations
    # the number 'stations_premise' from the premise is consistent with the hypothesis, but the exact number cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)
