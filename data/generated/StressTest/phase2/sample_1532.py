# Premise: Kiran travels from A to B by car and returns from B to A by cycle in 7 hours.
# Hypothesis: Kiran travels from A to B by car and returns from B to A by cycle in less than 7 hours.
# Golden Label: contradiction

travel_time_premise = 7
travel_time_hypothesis = 7

# the hypothesis refers to the time Kiran uses to travel from A to B and back, mentioned also in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the travel time in the hypothesis is less than the one in the premise, we can infer entailment
    label = "entailment"

print(label)

