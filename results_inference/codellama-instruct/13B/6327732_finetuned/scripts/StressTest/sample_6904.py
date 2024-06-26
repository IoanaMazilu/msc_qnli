premise_total_cost = 360
hypothesis_total_cost = 160

# the hypothesis refers to the total cost of renting the tool, which is mentioned in the premise
if hypothesis_total_cost <= premise_total_cost:
    # check if the estimate of 'hypothesis_total_cost' contradicts the total cost in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total cost
    # any total cost greater than 'premise_total_cost' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
