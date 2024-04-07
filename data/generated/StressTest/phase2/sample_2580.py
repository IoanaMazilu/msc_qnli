# Premise: By how much must Rebecca's yearly income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's yearly income increase so that it constitutes more than 15% of Rebecca and Jimmy's combined income?
# Golden Label: entailment

income_percentage_premise = 55
income_percentage_hypothesis = 15

# the hypothesis refers to the percentage of Rebecca's income increase in relation to Rebecca and Jimmy's combined income, also mentioned in the premise
if income_percentage_hypothesis >= income_percentage_premise:
    # check if the hypothesis value contradicts the percentage mentioned in the premise
    label = "contradiction"
elif income_percentage_hypothesis < income_percentage_premise:
    # the premise gives a specific percentage for Rebecca's income increase
    # any percentage less than 'income_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

