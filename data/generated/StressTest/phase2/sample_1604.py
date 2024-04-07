# Premise: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes more than 55% of Rebecca and Jimmy's combined income?
# Golden Label: contradiction

# The premise and hypothesis don't provide numerical quantities, but rather a comparison condition (55% or more than 55%).
# We can represent this condition using variables.
income_ratio_premise = 55
income_ratio_hypothesis = 55

# The hypothesis refers to the income ratio of Rebecca to the combined income of Rebecca and Jimmy.
# Since the premise and the hypothesis ask for the same income ratio (55%), but the hypothesis asks for more than this ratio,
# we can say that the hypothesis contradicts the premise.
if income_ratio_premise < income_ratio_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)

