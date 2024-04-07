# Premise: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in 1 hours.
# Golden Label: contradiction

travel_time_premise = 7
travel_time_hypothesis = 1

# the hypothesis mentions the same route and means of transportation as the premise
if travel_time_hypothesis == travel_time_premise:
    # check if the travel time in the hypothesis matches the travel time mentioned in the premise
    label = "entailment"
elif travel_time_hypothesis > travel_time_premise:
    # check if the travel time in the hypothesis contradicts the travel time mentioned in the premise
    label = "contradiction"
else:
    # if the travel time in the hypothesis does not contradict the premise, but also does not match it, we can infer neutrality
    label = "neutral"

print(label)

