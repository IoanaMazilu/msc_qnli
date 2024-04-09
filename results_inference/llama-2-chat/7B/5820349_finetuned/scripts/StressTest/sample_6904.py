rent_cost_premise = 360
rent_cost_hypothesis = 160

# the hypothesis talks about the cost of renting a tool, referenced also in the premise
if rent_cost_hypothesis >= rent_cost_premise:
    # check if the hypothesis value contradicts the estimate of less than'rent_cost_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the cost of renting
    # any cost less than'rent_cost_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
