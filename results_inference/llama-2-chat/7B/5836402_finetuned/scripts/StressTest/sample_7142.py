flights_departed_premise = 3
flights_departed_hypothesis = 3
departure_rate_premise = 0.5
departure_rate_hypothesis = 0.1

# the hypothesis refers to the number of flights and the departure rate mentioned in the premise
if flights_departed_hypothesis!= flights_departed_premise:
    # check if the number of flights in the hypothesis contradicts the number of flights reported in the premise
    label = "contradiction"
elif departure_rate_hypothesis > departure_rate_premise:
    # check if the departure rate in the hypothesis contradicts the departure rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
