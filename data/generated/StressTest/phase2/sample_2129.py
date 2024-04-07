# Premise: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers l did Carl drive each way?
# Hypothesis: If the trip home took more than 1/2 hour longer than the trip to the beach, how many kilometers l did Carl drive each way?
# Golden Label: contradiction

trip_time_difference_premise = 0.5
trip_time_difference_hypothesis = 0.5

# The hypothesis talks about the time difference between the trip home and to the beach, referenced also in the premise
if trip_time_difference_hypothesis > trip_time_difference_premise:
    # Check if the hypothesis value contradicts the exact time difference mentioned in the premise
    label = "contradiction"
elif trip_time_difference_hypothesis < trip_time_difference_premise:
    # Check if the hypothesis value contradicts the exact time difference mentioned in the premise
    label = "contradiction"
else:
    # The premise and hypothesis both talk about the same time difference, 
    # so the hypothesis does not contradict the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

