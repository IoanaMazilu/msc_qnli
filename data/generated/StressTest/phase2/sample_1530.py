# Premise: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in more than 6 hours.
# Golden Label: entailment

travel_time_premise = 7
travel_time_hypothesis = 6

# the hypothesis refers to the travel time mentioned in the premise
if travel_time_premise < travel_time_hypothesis:
    # check if the travel time in the premise contradicts the estimate of 'travel_time_hypothesis'
    label = "contradiction"
elif travel_time_premise == travel_time_hypothesis:
    # check if the travel time in the premise contradicts the estimate of 'travel_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

