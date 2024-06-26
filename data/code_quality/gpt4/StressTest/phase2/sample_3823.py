stations_premise = 26
stations_hypothesis = 16

# the hypothesis talks about the number of stations between Mumbai and Chennai, which is also referenced in the premise
if stations_hypothesis >= stations_premise:
    # check if the number of stations in the hypothesis contradicts the estimate of less than 'stations_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of stations
    # any number of stations less than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
