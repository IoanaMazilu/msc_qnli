# Premise: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes less than 55% of Rebecca and Jimmy's combined income?
# Golden Label: contradiction

income_percentage_premise = 55
income_percentage_hypothesis = 55

# the hypothesis is about the necessary increase in Rebecca's annual income to reach a certain percentage of the combined income
# which is also referenced in the premise
if income_percentage_hypothesis >= income_percentage_premise:
    # check if the hypothesis percentage contradicts the premise percentage
    label = "contradiction"
else:
    # the premise and hypothesis are about the same situation but estimate different percentages
    # the hypothesis percentage cannot be explicitly entailed from the premise, but also does not contradict it
    label = "neutral"

print(label)

