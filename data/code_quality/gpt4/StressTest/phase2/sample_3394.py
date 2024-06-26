stations_premise = 60
stations_hypothesis = 10

# the hypothesis is referring to the number of stations between Hyderabad and Bangalore, as mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
