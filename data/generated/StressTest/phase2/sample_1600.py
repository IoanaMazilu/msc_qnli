# Premise: Rebecca's annual income is $less than 55 and Jimmy's annual income is $18.
# Hypothesis: Rebecca's annual income is $15 and Jimmy's annual income is $18.
# Golden Label: neutral

rebecca_income_premise = 55
jimmy_income_premise = 18
rebecca_income_hypothesis = 15
jimmy_income_hypothesis = 18

# the hypothesis talks about the annual incomes of Rebecca and Jimmy, which are also mentioned in the premise
if rebecca_income_hypothesis >= rebecca_income_premise:
    # check if the hypothesis value for Rebecca's income contradicts the premise
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the hypothesis value for Jimmy's income contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

