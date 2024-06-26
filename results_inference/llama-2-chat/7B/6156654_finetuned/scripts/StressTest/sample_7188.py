departure_time_premise = 12
departure_time_hypothesis = 42

# the hypothesis talks about the departure time of a train, which is also mentioned in the premise
if departure_time_hypothesis >= departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time in the premise
    label = "contradiction"
elif departure_time_hypothesis < departure_time_premise:
    # if the departure time in the hypothesis is less than the departure time in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the departure time in the hypothesis is equal to the departure time in the premise, it is neutral
    label = "neutral"

print(label)
