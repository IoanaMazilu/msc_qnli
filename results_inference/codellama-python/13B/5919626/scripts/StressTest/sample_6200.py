stations_hyderabad_bangalore_premise = 18
stations_hyderabad_bangalore_hypothesis = 88

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hyderabad_bangalore_hypothesis <= stations_hyderabad_bangalore_premise:
    # check if the hypothesis value contradicts the estimate of more than'stations_hyderabad_bangalore_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations between Hyderabad and Bangalore
    # any number of stations between Hyderabad and Bangalore greater than'stations_hyderabad_bangalore_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
