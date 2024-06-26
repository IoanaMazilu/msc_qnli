bonds_value_premise = 3500
bonds_value_hypothesis = 7500

# the hypothesis refers to Robert's purchases of US saving bonds, also mentioned in the premise
if bonds_value_hypothesis < bonds_value_premise:
    # check if the estimate in the hypothesis contradicts the exact value in the premise
    label = "contradiction"
elif bonds_value_premise > bonds_value_hypothesis:
    # check if the value in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # the premise gives a specific value for the worth of US saving bonds Robert purchased
    # any worth less than 'bonds_value_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
