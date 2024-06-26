children_premise = 25.0
children_got_on = 18.0
children_hypothesis = 43.0

# the hypothesis refers to the number of children riding on the bus, which are also mentioned in the premise
# compute the total number of children riding on the bus in the premise
total_children_premise = children_premise + children_got_on
if children_hypothesis!= total_children_premise:
    # check if the number of children in the hypothesis contradicts the number of children from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
