rebecca_income_premise = 15
jimmy_income_premise = 18
rebecca_income_hypothesis = 45
jimmy_income_hypothesis = 18

# the hypothesis talks about the annual incomes of Rebecca and Jimmy, which are also mentioned in the premise
if rebecca_income_hypothesis <= rebecca_income_premise:
    # check if the hypothesis value contradicts the exact value of 'rebecca_income_premise'
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the hypothesis value contradicts the exact value of 'jimmy_income_premise'
    label = "contradiction"
else:
    # the premise gives exact values for the annual incomes
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
