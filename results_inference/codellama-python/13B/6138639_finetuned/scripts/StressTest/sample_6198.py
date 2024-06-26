stations_premise = 18
stations_hypothesis = 48

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_premise >= stations_hypothesis:
    # check if the premise value contradicts the estimate of less than'stations_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of stations
    # any number of stations less than'stations_hypothesis' is consistent with the premise, and can be explicitly entailed from the premise
    label = "entailment"

print(label)
