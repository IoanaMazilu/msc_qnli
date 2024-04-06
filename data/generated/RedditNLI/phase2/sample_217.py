# Premise: Pfizer nears deal to acquire Medivation for close to US$14b.
# Hypothesis: Pfizer to Buy Medivation for $14 Billion.
# Golden Label: entailment

deal_value_premise = 14
deal_value_hypothesis = 14

# the hypothesis and premise mention the deal value for Pfizer's acquisition of Medivation
if deal_value_premise != deal_value_hypothesis:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the deal value in the hypothesis does not contradict the deal value in the premise, we can infer entailment
    label = "entailment"

print(label)

