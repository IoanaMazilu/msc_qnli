fuel_spilled_premise = 28
fuel_spilled_hypothesis = 28

# the hypothesis mentions the amount of fuel spilled, which is also mentioned in the premise
if fuel_spilled_hypothesis != fuel_spilled_premise:
    # check if the fuel spilled in the hypothesis contradicts the fuel spilled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis amount of fuel spilled does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
