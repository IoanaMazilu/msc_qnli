children_on_bus_premise = 25.0
children_got_on_premise = 18.0
children_on_bus_hypothesis = 39.0

# the hypothesis refers to the number of children on the bus after some got on at the bus stop, which is also mentioned in the premise
# compute the total number of children on the bus in the premise
total_children_on_bus_premise = children_on_bus_premise + children_got_on_premise
if children_on_bus_hypothesis != total_children_on_bus_premise:
    # check if the number of children on the bus in the hypothesis contradicts the number of children on the bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
