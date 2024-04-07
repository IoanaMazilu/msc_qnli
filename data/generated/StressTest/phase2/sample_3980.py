# Premise: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Hypothesis: If the trip home took more than 1/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Golden Label: contradiction

trip_home_premise = 0.5
trip_home_hypothesis = 0.5

# the hypothesis refers to the duration of the trip home in relation to the trip to the beach, also mentioned in the premise
if trip_home_hypothesis > trip_home_premise:
    # check if the hypothesis value contradicts the duration of the trip home in the premise
    label = "contradiction"
elif trip_home_hypothesis < trip_home_premise:
    # check if the hypothesis value contradicts the duration of the trip home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

