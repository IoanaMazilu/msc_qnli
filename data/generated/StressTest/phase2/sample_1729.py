# Premise: Rebecca's annual income is $less than 45, and Jimmy's annual income is $18.
# Hypothesis: Rebecca's annual income is $15, and Jimmy's annual income is $18.
# Golden Label: neutral

rebecca_income_premise = 45
rebecca_income_hypothesis = 15
jimmy_income_premise = 18
jimmy_income_hypothesis = 18

# the hypothesis refers to the annual incomes of Rebecca and Jimmy, which are also mentioned in the premise
if rebecca_income_hypothesis >= rebecca_income_premise:
    # check if Rebecca's income in the hypothesis contradicts the premise of Rebecca's income being less than 'rebecca_income_premise'
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if Jimmy's income in the hypothesis contradicts the premise of Jimmy's income being exactly 'jimmy_income_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

