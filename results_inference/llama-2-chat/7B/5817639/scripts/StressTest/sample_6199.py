stations_premise = 48
stations_hypothesis = 18

# the hypothesis talks about the number of stations between two cities, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than'stations_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of stations, and the hypothesis value is consistent with it
    label = "entailment"

print(label)