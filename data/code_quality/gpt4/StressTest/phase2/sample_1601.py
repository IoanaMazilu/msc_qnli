rebecca_income_premise = 15
jimmy_income_premise = 18
rebecca_income_hypothesis = 55
jimmy_income_hypothesis = 18

# the hypothesis refers to the annual incomes of Rebecca and Jimmy mentioned in the premise
if rebecca_income_hypothesis != rebecca_income_premise:
    # check if the value of 'rebecca_income_hypothesis' contradicts the value of Rebecca's income in the premise
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the value of 'jimmy_income_hypothesis' contradicts the value of Jimmy's income in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
