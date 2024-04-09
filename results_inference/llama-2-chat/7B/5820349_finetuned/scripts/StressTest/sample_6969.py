stations_premise = 8
stations_hypothesis = 4

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_premise <= stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of more than'stations_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of stations
    # any number of stations less than'stations_premise' contradicts the premise
    label = "contradiction"

print(label)
