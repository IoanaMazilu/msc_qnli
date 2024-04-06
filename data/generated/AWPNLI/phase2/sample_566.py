# Premise: 25.0 children were riding on the bus and at the bus stop 18.0 children got on the bus.
# Hypothesis: 43.0 children are now riding on the bus.
# Golden Label: entailment

children_bus_premise = 25.0
children_bus_stop_premise = 18.0
children_bus_hypothesis = 43.0

# the hypothesis refers to the total number of children on the bus which is also referenced in the premise
# compute the total number of children on the bus in the premise
total_children_bus_premise = children_bus_premise + children_bus_stop_premise
if children_bus_hypothesis != total_children_bus_premise:
    # check if the number of children on the bus in the hypothesis contradicts the total number of children on the bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

