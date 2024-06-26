gas_reserves_control_premise = 0.20
gas_reserves_control_hypothesis = 0.20

# the hypothesis mentions the percentage of the world's natural gas reserves controlled by a company, which is also mentioned in the premise
if gas_reserves_control_hypothesis != gas_reserves_control_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
