# Premise: By how much must Rebecca's annual income increase so that it constitutes more than 45% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Golden Label: neutral

income_percentage_premise = 45
income_percentage_hypothesis = 55

# the hypothesis talks about the percentage of Rebecca's income in relation to the combined income of Rebecca and Jimmy, also referenced in the premise
if income_percentage_hypothesis <= income_percentage_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'income_percentage_premise'
    label = "contradiction"
elif income_percentage_hypothesis > income_percentage_premise:
    # the premise gives only an estimate for the percentage of Rebecca's income
    # a percentage greater than 'income_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

