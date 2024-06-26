departure_time_premise = 8
departure_time_hypothesis = 8

# the hypothesis refers to the departure time mentioned in the premise

if departure_time_hypothesis < departure_time_premise:
    # check if the hypothesis time contradicts the departure time in the premise
    label = "contradiction"
elif departure_time_hypothesis > departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
