# Premise: The federal government allows taxpayers a $500 exemption for housing victims of a Midwestern disaster.
# Hypothesis: If you house a victim of a Midwestern disaster, IRS offers $500 tax exemption.
# Golden Label: entailment

exemption_premise = 500
exemption_hypothesis = 500

# the hypothesis mentions the tax exemption amount for housing disaster victims, which is also mentioned in the premise
if exemption_hypothesis != exemption_premise:
    # check if the exemption amount in the hypothesis contradicts the exemption amount reported in the premise
    label = "contradiction"
else:
    # if the exemption amount in the hypothesis does not contradict the exemption amount in the premise, we can infer entailment
    label = "entailment"

print(label)

