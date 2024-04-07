# Premise: Kiran travels from A to B by car and returns from B to A by cycle in less than 8 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Golden Label: neutral

travel_time_premise = 8
travel_time_hypothesis = 7

# the hypothesis refers to the same travel from A to B and back to A mentioned in the premise
if travel_time_hypothesis > travel_time_premise:
    # check if the estimated 'travel_time_hypothesis' contradicts the premise
    label = "contradiction"
elif travel_time_hypothesis < travel_time_premise:
    # if the travel time in the hypothesis is less than the time mentioned in the premise
    # we can infer that the hypothesis is entailed from the premise
    label = "entailment"
else:
    # if the travel time in the hypothesis matches the time mentioned in the premise
    # we can infer that the hypothesis is entailed from the premise
    label = "entailment"
    
print(label)

