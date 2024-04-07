# Premise: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes more than 15% of Rebecca and Jimmy's combined income?
# Golden Label: entailment

income_percentage_premise = 55
income_percentage_hypothesis = 15

# the hypothesis refers to the percentage of the combined income that Rebecca's income should represent
if income_percentage_hypothesis >= income_percentage_premise:
    # check if the required percentage in 'income_percentage_hypothesis' contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

