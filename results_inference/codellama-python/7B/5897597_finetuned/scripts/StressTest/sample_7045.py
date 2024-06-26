travel_time_premise = 20
travel_time_hypothesis = 10

# the hypothesis talks about the travel time of Raman, referenced also in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time less than 'travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
