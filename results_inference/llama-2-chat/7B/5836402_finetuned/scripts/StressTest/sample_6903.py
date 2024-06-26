tool_rent_cost_premise = 160
tool_rent_cost_hypothesis = 360

# the hypothesis refers to the cost of renting the tool, which is also mentioned in the premise
if tool_rent_cost_premise >= tool_rent_cost_hypothesis:
    # check if the estimate of 'tool_rent_cost_hypothesis' contradicts the cost of tool rent in the premise
    label = "contradiction"
elif tool_rent_cost_hypothesis < tool_rent_cost_premise:
    # check if the cost of tool rent in the hypothesis contradicts the cost of tool rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
