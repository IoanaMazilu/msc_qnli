premise_travel_time = 10
hypothesis_travel_time = 20

# the hypothesis refers to the travel time mentioned in the premise
if premise_travel_time <= hypothesis_travel_time:
    # check if the hypothesis value contradicts the estimate of 'premise_travel_time'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time less than 'premise_travel_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
