total_cost_premise = 160
total_cost_hypothesis = 760

# the hypothesis refers to the total cost of renting the tool, which is also mentioned in the premise
if total_cost_hypothesis <= total_cost_premise:
    # check if the estimate of 'total_cost_hypothesis' contradicts the total cost in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total cost
    # any total cost greater than 'total_cost_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
