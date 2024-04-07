# Premise: Rebecca's annual income is $15 and Jimmy's annual income is $18.
# Hypothesis: Rebecca's annual income is $less than 55 and Jimmy's annual income is $18.
# Golden Label: entailment

rebecca_income_premise = 15
jimmy_income_premise = 18
rebecca_income_hypothesis = 55
jimmy_income_hypothesis = 18

# the hypothesis refers to the annual incomes of Rebecca and Jimmy, mentioned in the premise
if rebecca_income_premise >= rebecca_income_hypothesis:
    # check if the estimate of 'rebecca_income_hypothesis' contradicts the income of Rebecca in the premise
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the income of Jimmy in the hypothesis contradicts the income of Jimmy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

