departure_time_premise = 9
departure_time_hypothesis = 1

# the hypothesis refers to the departure time of a train from Delhi, also mentioned in the premise
if departure_time_hypothesis!= departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time mentioned in the premise
    label = "contradiction"
else:
    # if the departure times in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
