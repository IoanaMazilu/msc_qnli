# Premise: By how much must Rebecca's annual income increase so that it constitutes 55% of Rebecca and Jimmy's combined income?
# Hypothesis: By how much must Rebecca's annual income increase so that it constitutes more than 45% of Rebecca and Jimmy's combined income?
# Golden Label: entailment

income_percentage_premise = 55
income_percentage_hypothesis = 45

# the hypothesis refers to the percentage of income increase for Rebecca mentioned in the premise
if income_percentage_hypothesis >= income_percentage_premise:
    # check if the percentage of 'income_percentage_hypothesis' contradicts the percentage of income increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

