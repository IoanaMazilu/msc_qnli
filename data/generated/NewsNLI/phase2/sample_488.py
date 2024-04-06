# Premise: It controls 20 percent of the world's natural gas reserves and operates the world's largest gas distribution network -- approximately 157,000 kilometers of pipelines covering an area from Europe to the Far East, according to its Web site.
# Hypothesis: Gazprom controls 20 percent of world's natural gas reserves.
# Golden Label: neutral

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

