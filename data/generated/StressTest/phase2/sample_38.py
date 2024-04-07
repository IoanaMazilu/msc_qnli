# Premise: Louie takes out a three-month loan of $1000.
# Hypothesis: Louie takes out a three-month loan of $8000.
# Golden Label: contradiction

loan_premise = 1000
loan_hypothesis = 8000

# the hypothesis talks about a loan mentioned in the premise
if loan_hypothesis != loan_premise:
    # check if the value of the loan in the hypothesis contradicts the value of the loan reported in the premise
    label = "contradiction"
else:
    # if the loan value in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

