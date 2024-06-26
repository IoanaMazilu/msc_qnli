trip_to_beach_premise = 1/2
trip_home_premise = 1/2
trip_to_beach_hypothesis = 4/2
trip_home_hypothesis = 4/2

# the hypothesis refers to the time taken for the trip home and the trip to the beach, which are also mentioned in the premise
if trip_home_hypothesis!= trip_home_premise:
    # check if the time taken for the trip home in the hypothesis contradicts the time taken for the trip home in the premise
    label = "contradiction"
elif trip_to_beach_hypothesis!= trip_to_beach_premise:
    # check if the time taken for the trip to the beach in the hypothesis contradicts the time taken for the trip to the beach in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
