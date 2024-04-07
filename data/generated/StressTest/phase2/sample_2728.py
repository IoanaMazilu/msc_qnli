# Premise: Rebecca's annual income is $less than 50, and Jimmy's annual income is $10 ,
# Hypothesis: Rebecca's annual income is $20, and Jimmy's annual income is $10 ,
# Golden Label: neutral

rebecca_income_premise = 50
rebecca_income_hypothesis = 20
jimmy_income_premise = 10
jimmy_income_hypothesis = 10

# the hypothesis refers to the annual incomes of Rebecca and Jimmy mentioned in the premise
if rebecca_income_hypothesis >= rebecca_income_premise:
    # check if 'rebecca_income_hypothesis' contradicts the estimate of less than 'rebecca_income_premise' in the premise
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the annual income of Jimmy in the hypothesis contradicts his annual income in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

