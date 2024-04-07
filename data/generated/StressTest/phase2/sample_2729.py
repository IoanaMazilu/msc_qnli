# Premise: Rebecca's annual income is $20, and Jimmy's annual income is $10 ,
# Hypothesis: Rebecca's annual income is $more than 20, and Jimmy's annual income is $10 ,
# Golden Label: contradiction

rebecca_income_premise = 20
jimmy_income_premise = 10
rebecca_income_hypothesis = 20
jimmy_income_hypothesis = 10

# the hypothesis talks about the annual income of Rebecca and Jimmy, referenced also in the premise
if rebecca_income_hypothesis >= rebecca_income_premise:
    # check if the hypothesis value contradicts the value of 'rebecca_income_premise'
    label = "contradiction"
elif jimmy_income_hypothesis != jimmy_income_premise:
    # check if the annual income of Jimmy in the hypothesis contradicts the annual income of Jimmy presented in the premise
    label = "contradiction"
else:
    # the premise gives exact figures for the annual income of Rebecca and Jimmy
    # any claim that Rebecca's income is more than the given figure in the premise and Jimmy's income is exactly the same as in the premise is a contradiction
    label = "contradiction"

print(label)

