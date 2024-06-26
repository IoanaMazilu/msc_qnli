train_departure_premise = 12
train_departure_hypothesis = 42

# the hypothesis refers to the time of departure of a train from Jammu to Chennai, also mentioned in the premise
if train_departure_hypothesis >= train_departure_premise:
    # check if the hypothesis value contradicts the premise of exact departure time of 12 noon
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
