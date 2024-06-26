tool_rental_cost_premise = 160
tool_rental_cost_hypothesis = 760

# the hypothesis refers to the cost of renting the tool, which is also mentioned in the premise
if tool_rental_cost_hypothesis!= tool_rental_cost_premise:
    # check if the cost of renting the tool in the hypothesis contradicts the cost mentioned in the premise
    label = "contradiction"
else:
    # if the cost of renting the tool in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
