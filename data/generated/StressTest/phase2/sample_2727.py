# Premise: Rebecca's annual income is $20, and Jimmy's annual income is $10 ,
# Hypothesis: Rebecca's annual income is $less than 50, and Jimmy's annual income is $10 ,
# Golden Label: entailment

rebecca_income_premise = 20
rebecca_income_hypothesis = 50
jimmy_income_premise = 10
jimmy_income_hypothesis = 10

# the hypothesis refers to the annual incomes of Rebecca and Jimmy mentioned in the premise
if rebecca_income_premise > rebecca_income_hypothesis:
    # check if 'rebecca_income_premise' contradicts the limit set by 'rebecca_income_hypothesis'
    label = "contradiction"
elif jimmy_income_premise != jimmy_income_hypothesis:
    # check if 'jimmy_income_premise' contradicts 'jimmy_income_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

