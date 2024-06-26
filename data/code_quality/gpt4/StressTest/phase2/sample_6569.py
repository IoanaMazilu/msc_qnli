trip_home_premise = 0.5
trip_home_hypothesis = 0.5

# The hypothesis refers to the trip duration mentioned in the premise
if trip_home_premise < trip_home_hypothesis:
    # Check if the estimated 'trip_home_hypothesis' contradicts the trip duration in the premise
    label = "contradiction"
elif trip_home_premise > trip_home_hypothesis:
    # Check if the trip duration in the hypothesis contradicts the estimated trip duration in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
