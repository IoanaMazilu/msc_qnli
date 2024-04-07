# Premise: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?
# Hypothesis: If the trip home took 4/2 hour longer than the trip to the beach, how many kilometers o did Carl drive each way?
# Golden Label: contradiction

trip_home_premise = 1/2
trip_home_hypothesis = 4/2

# the hypothesis refers to the duration of the trip home mentioned in the premise
if trip_home_premise != trip_home_hypothesis:
    # check if the trip home duration in the hypothesis contradicts the trip home duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

