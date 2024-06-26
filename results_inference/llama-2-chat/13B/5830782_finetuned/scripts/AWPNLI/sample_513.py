trip_distance_premise = 256.0
trips_number_premise = 32.0
total_distance_hypothesis = 8191.0

# the hypothesis refers to the total distance flown, which can be computed from the premise
# compute the total distance flown in the premise
total_distance_premise = trip_distance_premise * trips_number_premise
if total_distance_hypothesis!= total_distance_premise:
    # check if the total distance flown in the hypothesis contradicts the total distance flown from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)