rebecca_income_premise = 15
jimmy_income_premise = 18
rebecca_income_hypothesis = 15
jimmy_income_hypothesis = 18

# the hypothesis refers to the annual incomes of Rebecca and Jimmy mentioned in the premise
if rebecca_income_hypothesis >= rebecca_income_premise:
    # check if the estimate of 'rebecca_income_hypothesis' contradicts the income of Rebecca in the premise
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the income of Jimmy in the hypothesis contradicts the income of Jimmy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
