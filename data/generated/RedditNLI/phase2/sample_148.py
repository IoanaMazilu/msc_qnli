# Premise: U.S. Second-Quarter Growth Revised Up to 4.2% on Software, Trade.
# Hypothesis: U.S. second-quarter GDP growth raised to 4.2 percent.
# Golden Label: entailment

growth_rate_premise = 4.2
growth_rate_hypothesis = 4.2

# the hypothesis and premise both mention the revised growth rate for U.S. second-quarter
if growth_rate_premise != growth_rate_hypothesis:
    # check if the growth rate in the hypothesis contradicts the growth rate in the premise
    label = "contradiction"
else:
    # if the growth rate in the hypothesis does not contradict the growth rate in the premise, we can infer entailment
    label = "entailment"

print(label)

