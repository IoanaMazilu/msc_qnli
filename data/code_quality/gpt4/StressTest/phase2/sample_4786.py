stations_premise = 65
stations_hypothesis = 25

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
elif stations_hypothesis < stations_premise:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
