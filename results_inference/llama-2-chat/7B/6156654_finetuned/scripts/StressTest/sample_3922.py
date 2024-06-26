departure_time_premise = 4
departure_time_hypothesis = 9

# the hypothesis talks about the departure time of a train from Delhi, which is also mentioned in the premise
if departure_time_hypothesis <= departure_time_premise:
    # check if the departure time in the hypothesis contradicts the premise
    label = "contradiction"
elif departure_time_hypothesis > departure_time_premise:
    # check if the departure time in the hypothesis entails the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict or entail the premise ones, we can infer neutral
    label = "neutral"

print(label)
