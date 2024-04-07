# Premise: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in more than 7 hours.
# Golden Label: contradiction

travel_time_premise = 7
travel_time_hypothesis = 7

# the hypothesis refers to the same travel time as in the premise
if travel_time_hypothesis > travel_time_premise:
    # check if the hypothesis value contradicts the exact time of 'travel_time_premise' hours reported in the premise
    label = "contradiction"
elif travel_time_hypothesis < travel_time_premise:
    # check if the hypothesis value contradicts the exact time of 'travel_time_premise' hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and the reported time in the premise match, we can infer entailment
    label = "entailment"

print(label)

