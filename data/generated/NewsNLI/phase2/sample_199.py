# Premise: And regardless of how safe we make oil drilling, tankers, or pipelines, we'll never reduce spill risk to zero.
# Hypothesis: She says no matter how we make drilling, tankers, pipelines safe, risk will never be zero.
# Golden Label: entailment

risk_reduction_premise = 0
risk_reduction_hypothesis = 0

# the hypothesis mentions that the risk of oil spills will never be zero, which is also mentioned in the premise
if risk_reduction_hypothesis != risk_reduction_premise:
    # check if the risk reduction in the hypothesis contradicts the risk reduction reported in the premise
    label = "contradiction"
else:
    # if the risk reduction values from the hypothesis do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

