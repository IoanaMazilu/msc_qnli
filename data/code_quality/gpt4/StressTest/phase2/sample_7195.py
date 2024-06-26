train_travel_time_premise = 6*24*60 + 1  # converting days into minutes
train_travel_time_hypothesis = 7*24*60 + 1  # converting days into minutes

# the hypothesis talks about the time required by a train to cover a distance, referenced also in the premise
if train_travel_time_hypothesis <= train_travel_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'train_travel_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel time
    # any travel time greater than 'train_travel_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
